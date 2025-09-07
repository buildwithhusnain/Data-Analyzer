# Data Analyzer

A modern, responsive Flask web application for uploading and visualizing data from CSV and Excel files. Transform your data into stunning interactive visualizations with just a few clicks.

![Data Analyzer](https://img.shields.io/badge/Flask-2.3.3-blue)
![Python](https://img.shields.io/badge/Python-3.9+-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## ✨ Features

- **📁 File Upload**: Support for CSV, XLS, and XLSX files (up to 16MB)
- **📊 Interactive Charts**: Create bar charts, line charts, pie charts, scatter plots, and histograms
- **🎨 Modern UI**: Clean, responsive design using Tailwind CSS
- **📱 Mobile Friendly**: Works seamlessly on desktop and mobile devices
- **🖱️ Drag & Drop**: Intuitive file upload with drag and drop functionality
- **👀 Data Preview**: Instant dataset overview and sample data display
- **⚡ Real-time**: Dynamic chart generation based on your data

## 🚀 Quick Start

### Local Installation

1. **Clone the repository**
```bash
git clone https://github.com/buildwithhusnain/Data-Analyzer.git```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
python app.py
```

4. **Open your browser** and go to `http://localhost:5000`

### Docker Installation

1. **Using Docker Compose (Recommended)**
```bash
docker-compose up --build
```

2. **Using Docker directly**
```bash
docker build -t data-analyzer .
docker run -p 5000:5000 data-analyzer
```

## 📖 Usage

1. **Upload**: Drag and drop your CSV or Excel file, or click to browse
2. **Analyze**: Click "Upload & Analyze" to process your data
3. **Visualize**: Select chart type and columns to create custom visualizations
4. **Explore**: View dataset overview, data preview, and interactive charts
5. **Repeat**: Use "Upload New File" to analyze different datasets

## 📋 Supported File Types

- **CSV** (.csv) - Comma-separated values
- **Excel** (.xlsx, .xls) - Microsoft Excel files

## 📊 Chart Types

| Chart Type | Best For | Requirements |
|------------|----------|-------------|
| **Bar Chart** | Categorical vs Numeric data | X: Categorical, Y: Numeric |
| **Line Chart** | Trends over time/sequence | X: Numeric/Date, Y: Numeric |
| **Pie Chart** | Distribution of categories | X: Categorical |
| **Scatter Plot** | Correlation between variables | X: Numeric, Y: Numeric |
| **Histogram** | Distribution of numeric data | X: Numeric |

## 🛠️ Technology Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML5, Tailwind CSS, JavaScript
- **Charts**: Plotly.js
- **Data Processing**: Pandas
- **File Handling**: Werkzeug

## 📁 Project Structure

```
data-analyzer/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── Dockerfile            # Docker configuration
├── docker-compose.yml    # Docker Compose setup
├── templates/
│   └── index.html        # Main HTML template
├── uploads/              # File upload directory
├── static/               # Static assets (if any)
└── README.md            # Project documentation
```

## 🔧 Configuration

- **Max file size**: 16MB (configurable in `app.py`)
- **Allowed extensions**: CSV, XLS, XLSX
- **Upload directory**: `uploads/` (auto-created)

## 🚀 Deployment

### Heroku
```bash
# Add Procfile
echo "web: python app.py" > Procfile

# Deploy
heroku create your-app-name
git push heroku main
```

### Railway/Render
- Connect your GitHub repository
- Set build command: `pip install -r requirements.txt`
- Set start command: `python app.py`

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🐛 Issues & Support

If you encounter any issues or have questions:
- Open an issue on GitHub
- Check existing issues for solutions
- Provide detailed information about your problem

## 🎯 Roadmap

- [ ] Add more chart types (box plots, heatmaps)
- [ ] Export charts as images
- [ ] Data filtering and sorting
- [ ] Multiple file upload
- [ ] User authentication
- [ ] Data persistence

---

**Made with ❤️ using Flask and Plotly**
