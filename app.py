from flask import Flask, render_template, request, jsonify, redirect, url_for
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.utils
import json
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Create uploads directory if it doesn't exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

ALLOWED_EXTENSIONS = {'csv', 'xlsx', 'xls'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def load_data(filepath):
    """Load data from CSV or Excel file"""
    try:
        if filepath.endswith('.csv'):
            return pd.read_csv(filepath)
        else:
            return pd.read_excel(filepath)
    except Exception as e:
        return None

def create_chart(df, chart_type, x_col, y_col=None):
    """Create a single chart based on user selection"""
    colors = ['#3b82f6', '#8b5cf6', '#10b981', '#f59e0b', '#ef4444']
    
    if chart_type == 'bar':
        fig = px.bar(df, x=x_col, y=y_col, color_discrete_sequence=colors)
        fig.update_layout(title=f'{y_col} by {x_col}')
    elif chart_type == 'line':
        fig = px.line(df, x=x_col, y=y_col, color_discrete_sequence=colors)
        fig.update_layout(title=f'{y_col} vs {x_col}')
    elif chart_type == 'scatter':
        fig = px.scatter(df, x=x_col, y=y_col, color_discrete_sequence=colors)
        fig.update_layout(title=f'{y_col} vs {x_col} Scatter Plot')
    elif chart_type == 'pie':
        value_counts = df[x_col].value_counts()
        fig = px.pie(values=value_counts.values, names=value_counts.index, color_discrete_sequence=colors)
        fig.update_layout(title=f'Distribution of {x_col}')
    elif chart_type == 'histogram':
        fig = px.histogram(df, x=x_col, color_discrete_sequence=colors)
        fig.update_layout(title=f'Distribution of {x_col}')
    
    fig.update_layout(plot_bgcolor='white', paper_bgcolor='white', font_color='black')
    return json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file selected'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Load and process data
        df = load_data(filepath)
        if df is None:
            return jsonify({'error': 'Failed to load file'}), 400
        
        # Get column information
        numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
        categorical_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
        all_cols = df.columns.tolist()
        
        # Get basic info about the dataset
        info = {
            'rows': len(df),
            'columns': len(df.columns),
            'column_names': all_cols,
            'numeric_columns': numeric_cols,
            'categorical_columns': categorical_cols,
            'data_types': df.dtypes.astype(str).to_dict()
        }
        
        return jsonify({
            'success': True,
            'info': info,
            'preview': df.head().to_html(classes='table-auto w-full text-sm', table_id='data-preview')
        })
    
    return jsonify({'error': 'Invalid file type'}), 400

@app.route('/create_chart', methods=['POST'])
def create_chart_endpoint():
    data = request.get_json()
    chart_type = data.get('chart_type')
    x_col = data.get('x_column')
    y_col = data.get('y_column')
    
    # Load the most recent file (in a real app, you'd store this per session)
    upload_dir = app.config['UPLOAD_FOLDER']
    files = [f for f in os.listdir(upload_dir) if allowed_file(f)]
    if not files:
        return jsonify({'error': 'No data file found'}), 400
    
    latest_file = max([os.path.join(upload_dir, f) for f in files], key=os.path.getctime)
    df = load_data(latest_file)
    
    if df is None:
        return jsonify({'error': 'Failed to load data'}), 400
    
    try:
        chart_json = create_chart(df, chart_type, x_col, y_col)
        return jsonify({'success': True, 'chart': chart_json})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)