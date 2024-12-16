# claude-project-xml

A Python-based GUI application for creating and managing XML project files in Claude's format. This tool helps you bundle multiple source files into a single XML configuration file that can be used as context for Claude (Anthropic's AI assistant). It's perfect for preparing multi-file projects for Claude interactions, creating reproducible examples, or bundling code for AI assistance.

This project specifically implements the XML format that Claude uses to process multiple files as context. When you provide this XML format to Claude, it can read and understand all the files in your project, making it easier to get help with complex, multi-file projects.

## Features

- **Intuitive GUI Interface**: Simple and clean interface for managing your project files
- **Drag & Drop Support**: Easily add multiple files by dragging them from your file explorer
- **Smart File Handling**: 
  - Automatic duplicate detection
  - Handles both text and binary files
  - Preserves file contents for text files under 1MB
- **Project Management**:
  - Save projects as XML files
  - Open existing project files
  - Clear and start fresh with a single click
- **XML Format**: Creates structured XML files with source paths and optional content embedding

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/claude-project-xml.git
cd claude-project-xml
```

2. Install required dependencies:
```bash
pip install tkinterdnd2
```

## Usage

Run the application:
```bash
python claude-project-xml.py
```

### Adding Files

There are two ways to add files to your project:
1. Click the "+ Add Files" button and select files using the file dialog
2. Drag and drop files directly from your file explorer into the application window

### Creating XML Projects

1. Add all desired files to the project
2. Click "Save XML" 
3. Choose a save location (defaults to "project.xml")

### Loading Existing Projects

1. Click "Open XML"
2. Select an existing project XML file
3. The application will load all referenced files

### Claude XML Format

The generated XML follows Claude's expected structure for processing multiple files. This is the official format used when providing multiple files as context to Claude:
```xml
<project>
    <document>
        <source>path/to/file1.txt</source>
        <document_content>Content of file1 if available</document_content>
    </document>
    <document>
        <source>path/to/file2.py</source>
        <document_content>Content of file2 if available</document_content>
    </document>
</project>
```

## Requirements

- Python 3.6+
- tkinterdnd2

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

To contribute:
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Uses `tkinterdnd2` for drag and drop functionality
- XML format based on Claude's (Anthropic's AI assistant) multi-file context specification
- Created to simplify the process of preparing multi-file projects for Claude interactions

## Related Links

- [Claude (by Anthropic)](https://www.anthropic.com/claude)
- [Claude Documentation](https://docs.anthropic.com/)

## Support

If you encounter any problems or have suggestions, please open an issue on the GitHub repository.