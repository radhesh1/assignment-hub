const { execSync } = require('child_process');
const fs = require('fs');

// Check if Flask is installed
try {
    execSync('flask --version');
    console.log('Flask is already installed.');
} catch (error) {
    console.log('Flask is not installed. Installing...');
    try {
        execSync('pip install Flask');
        console.log('Flask has been successfully installed.');
    } catch (error) {
        console.error('Failed to install Flask. Please install it manually using "pip install Flask".');
        process.exit(1);
    }
}

// Command to start Flask server
const flaskServerCommand = 'python3 app.py';

// Execute the Flask server command
const flaskServer = execSync(flaskServerCommand, { stdio: 'inherit' });
