# CSJoshC Learning Platform

A comprehensive learning platform built with **Docusaurus** featuring interactive content, dynamic layouts, and modern UI components.

## Features

- **Python Learning Paths** - From basics to advanced data science
- **General CS Topics** - CS50x, web development, and more
- **Modern UI** - Responsive design with light/dark mode
- **Mobile-First** - Works beautifully on all devices
- **Interactive Content** - Tabs, cards, progress tracking
- **Fast Performance** - Static site generation with Docusaurus
- **Jupyter Notebooks** - Interactive Python learning with live code execution
- **Blog & Site Updates** - Comprehensive learning journey documentation

## Quick Start

### Prerequisites

- **Node.js** (version 18 or higher) - For Docusaurus
- **npm** (comes with Node.js)
- **Python 3.9+** - For Jupyter notebooks and data science

### Installation

#### 1. Clone and Setup

```bash
# Clone the repository
git clone https://github.com/csjoshc/csjoshc.github.io.git
cd csjoshc.github.io

# Install Node.js dependencies (Docusaurus)
npm install
```

#### 2. Python Environment Setup

```bash
# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate  # macOS/Linux
# .venv\Scripts\activate   # Windows

# Install Python dependencies
pip install -r requirements.txt
```

### Development

#### Start Docusaurus (Web Interface)

```bash
# Start development server
npm start

# Open http://localhost:3000 in your browser
```

#### Blog Management

```bash
# Create new blog post
just blog-new "Post Title"

# List all blog posts
just blog-list

# Validate blog content
just blog-validate

# Start blog-focused development server
just blog-serve
```

#### Start Jupyter (Python Learning)

```bash
# Activate virtual environment
source .venv/bin/activate

# Start Jupyter Lab
jupyter lab

# Or start classic Jupyter Notebook
jupyter notebook
```

### Production Build

```bash
# Build for production
npm run build

# Preview production build
npm run serve

# Deploy to GitHub Pages
npm run deploy
```

## Project Structure

```
csjoshc.github.io/
├── docs/                    # Main content (markdown files)
│   ├── index.md            # Landing page with dynamic UI
│   ├── Python/             # Python learning materials
│   ├── General/            # General CS topics
│   ├── Github/             # Git and GitHub guides
│   ├── Linux/              # Linux and command line
│   ├── Devops/             # DevOps practices
│   ├── utils/              # Utility tools and scripts
│   └── site_updates/       # Site development log
├── blog/                    # Blog posts and learning journey
│   ├── 2019/               # 2019 learning progress
│   ├── 2020/               # 2020 learning progress
│   ├── 2021/               # 2021 learning progress
│   ├── 2025/               # 2025 site updates
│   ├── authors.yml         # Blog author information
│   └── tags.yml            # Blog tag definitions
├── src/
│   └── css/
│       └── custom.css      # Custom styling
├── docusaurus.config.ts    # Docusaurus configuration
├── sidebars.ts             # Navigation sidebar
├── package.json            # Node.js dependencies
├── requirements.txt         # Python dependencies
├── .venv/                  # Python virtual environment
└── README.md               # This file
```

## Content Sections

### Python Learning Path

- **Data Science Fundamentals** - NumPy, Pandas, Matplotlib
- **Machine Learning** - Clustering, Decision Trees, Regression
- **Computer Science** - MIT Intro to Computer Science
- **Statistics & Probability** - Mathematical foundations

### General Topics

- **CS50x 2019** - Harvard's CS50 course materials
- **Web Development** - Flask, databases, modern practices
- **GitHub Mastery** - Version control and collaboration
- **Linux Journey** - Command line and system administration

### Blog & Learning Journey

- **Site Updates** - Development progress and technical insights
- **Learning Milestones** - Personal growth and project achievements
- **Technical Deep-Dives** - In-depth analysis of concepts and tools
- **Project Documentation** - Complete project lifecycles and lessons learned
- **Weekly Updates** - Regular progress tracking and reflection

## Technology Stack

### Frontend (Docusaurus)

- **Docusaurus 3.8.1** - Modern static site generator
- **React 19** - UI components and interactivity
- **TypeScript** - Type-safe configuration
- **CSS Grid & Flexbox** - Responsive layouts
- **GitHub Pages** - Hosting and deployment

### Backend (Python)

- **Jupyter Lab/Notebook** - Interactive Python environment
- **Pandas & NumPy** - Data manipulation and analysis
- **Matplotlib & Seaborn** - Data visualization
- **Scikit-learn** - Machine learning algorithms
- **nbconvert** - Notebook conversion for Docusaurus

## Customization

### Styling

- Edit `src/css/custom.css` for global styles
- Use CSS variables for consistent theming
- Responsive breakpoints for all devices

### Content

- Add new markdown files in `docs/` directory
- Update `sidebars.ts` for navigation
- Use Docusaurus components for interactive elements
- Create Jupyter notebooks for interactive Python content

### Blog Posts

- **Location**: `blog/YYYY/MM/YYYY-MM-DD-title.md`
- **Front Matter**: Include title, authors, tags, description, date
- **Truncation**: Use `<!-- truncate -->` for post summaries
- **Tags**: Define new tags in `blog/tags.yml`
- **Authors**: Add authors in `blog/authors.yml`
- **Navigation**: Blog automatically appears in main navigation

### Configuration

- Modify `docusaurus.config.ts` for site settings
- Update metadata, navigation, and plugins
- Configure GitHub Pages deployment

## Deployment

### GitHub Pages

```bash
# Build and deploy
npm run deploy

# The site will be available at:
# https://csjoshc.github.io
```

### Manual Deployment

```bash
# Build the site
npm run build

# Upload the 'build' folder to your web server
```

## Troubleshooting

### Common Issues

- **Port 3000 in use**: Kill existing processes or use different port
- **Build errors**: Check for syntax errors in markdown files
- **Missing dependencies**: Run `npm install` to reinstall packages
- **Python environment**: Ensure `.venv` is activated for Jupyter
- **Blog build errors**: Check for missing tags in `blog/tags.yml`
- **MDX compilation**: Validate markdown syntax with `just check-mdx`

### Development Tips

- Use `npm start` for live development with hot reload
- Use `jupyter lab` for interactive Python development
- Check browser console for JavaScript errors
- Validate markdown syntax before committing
- Use `just blog-validate` to check blog content
- Run `just check-mdx` to prevent MDX compilation errors

> **🤖 AI Agent Rules**: For comprehensive AI interaction patterns, automation script requirements, and terminal command safety protocols, see [`.cursor/rules/60-ai-interaction-patterns.mdc`](.cursor/rules/60-ai-interaction-patterns.mdc)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test with `npm start` (web) and `jupyter lab` (Python)
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

- **Issues**: Report bugs and feature requests on GitHub
- **Documentation**: Check Docusaurus docs for advanced features
- **Community**: Join the Docusaurus community for help

---

Built with ❤️ using [Docusaurus](https://docusaurus.io/) + [Jupyter](https://jupyter.org/)
