from IPython.display import display, HTML

def pretty_print(title, content, style='info'):
    """Display formatted output in a styled box with different themes

    Args:
        title (str): The title of the message box
        content (str): The content to display
        style (str): Theme style - 'info', 'success', 'warning', 'error', 'result', 'note'
    
    Usage Examples:
        pretty_print("Info", "Loading data...", style='info')
        pretty_print("Success!", "Model trained", style='success')
        pretty_print("Warning", "Low accuracy", style='warning')
        pretty_print("Error", "File not found", style='error')
        pretty_print("Results", "Score: 92%", style='result')
        pretty_print("Tip", "Try lr=0.001", style='note')
    """

    # Define color schemes - each theme has 3 colors:
    # - primary: main color (used in gradient start and left border)
    # - secondary: darker shade (used in gradient end)
    # - background: very light tint for the content area
    themes = {
        'info': {  # Blue theme - for general information
            'primary': '#17a2b8',     # Light blue
            'secondary': '#0e5a63',   # Dark blue
            'background': '#f8f9fa'   # Very light gray-blue
        },
        'success': {  # Green theme - for successful operations
            'primary': '#28a745',     # Light green
            'secondary': '#155724',   # Dark green
            'background': '#f8fff9'   # Very light green
        },
        'warning': {  # Yellow/Orange theme - for warnings
            'primary': '#ffc107',     # Bright yellow
            'secondary': '#e0a800',   # Dark yellow/orange
            'background': '#fffdf5'   # Very light yellow
        },
        'error': {  # Red theme - for errors or critical alerts
            'primary': '#dc3545',     # Light red
            'secondary': '#721c24',   # Dark red
            'background': '#fff5f5'   # Very light red/pink
        },
        'result': {  # Purple theme - for showing results/outputs
            'primary': '#6f42c1',     # Light purple
            'secondary': '#4e2c8e',   # Dark purple
            'background': '#faf5ff'   # Very light purple
        },
        'note': {  # Teal theme - for tips or additional notes
            'primary': '#20c997',     # Light teal
            'secondary': '#0d7a5f',   # Dark teal
            'background': '#f0fdf9'   # Very light teal
        }
    }

    # Get the selected theme, default to 'info' if style not found
    theme = themes.get(style, themes['info'])

    # Build the HTML with inline CSS styling
    html = f'''
    <div style="border-radius: 5px;
                margin: 10px 0;
                width: 20cm;
                max-width: 20cm;
                box-sizing: border-box;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
        
        <!-- Title bar with gradient background -->
        <div style="background: linear-gradient(90deg, {theme['primary']} 0%, {theme['secondary']} 100%);
                    padding: 10px 15px; 
                    border-radius: 5px 5px 0 0;">
            <strong style="color: white; font-size: 14px;">{title}</strong>
        </div>
        
        <!-- Content area with light background and colored left border -->
        <div style="background: {theme['background']}; 
                    padding: 10px 15px; 
                    border-radius: 0 0 5px 5px;
                    border-left: 3px solid {theme['primary']};">
            <div style="color: rgba(0,0,0,0.8); 
                        font-size: 12px; 
                        line-height: 1.5;">{content}</div>
        </div>
    </div>
    '''
    
    # Display the HTML in Jupyter notebook
    display(HTML(html))