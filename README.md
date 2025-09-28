# HWHC Ban Appeal System

A web-based ban appeal system for the **Hard Way Hacking and Coding** Discord server. This application provides a streamlined process for users to submit ban appeals through Discord OAuth authentication.

## Features

- Discord OAuth2 authentication
- Secure ban appeal submission form
- Character count validation (100-5000 characters)
- Dark theme UI
- Responsive design
- Multi-step process with clear status indication

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Discord Developer Application (for OAuth2)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/loredous/ban_appeal.git
cd ban_appeal
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure your Discord OAuth2 settings (environment variables or configuration file)

4. Run the application:
```bash
python -m ban_appeal
```

## Usage

1. Users navigate to the ban appeal page
2. Authenticate with Discord (read-only permissions for username/avatar)
3. Submit a detailed ban appeal (100-5000 characters required)
4. Appeals are processed by the moderation team

## Contributing

We welcome contributions to improve the ban appeal system! Please follow these steps:

### How to Contribute

1. **Fork the repository**
   - Click the "Fork" button at the top right of this repository
   - This creates a copy of the repo in your GitHub account

2. **Clone your fork**
   ```bash
   git clone https://github.com/your-username/ban_appeal.git
   cd ban_appeal
   ```

3. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **Make your changes**
   - Write clean, documented code
   - Follow existing code style and conventions
   - Test your changes thoroughly

5. **Commit your changes**
   ```bash
   git add .
   git commit -m "Add: brief description of your changes"
   ```

6. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Open a Pull Request**
   - Go to the original repository on GitHub
   - Click "New Pull Request"
   - Select your fork and branch
   - Provide a clear description of your changes
   - Submit the pull request

### Guidelines

- Keep pull requests focused on a single feature or bug fix
- Include tests if applicable
- Update documentation as needed
- Be respectful in discussions and code reviews

## Project Structure

```
ban_appeal/
├── src/
│   └── ban_appeal/
│       ├── __init__.py
│       ├── __main__.py      # Main application entry point
│       └── html_data.py     # HTML templates and styling
├── pyproject.toml           # Project configuration
├── uv.lock                 # Dependency lock file
└── README.md               # This file
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

For questions about the ban appeal process, please contact the Hard Way Hacking and Coding Discord server moderators.

For technical issues with this application, please open an issue on GitHub.

---

**Hard Way Hacking and Coding Discord Server**  
*Providing education and guidance in the Cybersecurity, Ethical Hacking, and Programming world.*
https://discord.gg/MwVE6KffFK
