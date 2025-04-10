# File-Transfer Application

A simple and secure file sharing app built with Node.js, Express, MongoDB, and Multer. This app allows users to upload files and optionally protect them with a password before sharing a download link.

## 🚀 Features

- Upload any file type securely  
- Optional password protection for downloads  
- Generate unique download links  
- Tracks download counts  
- Passwords hashed using bcrypt

## 🛠️ Tech Stack

- Node.js & Express.js – Backend server  
- MongoDB & Mongoose – File metadata storage  
- Multer – File upload handling  
- bcrypt – Password hashing  
- dotenv – Environment variable management  
- EJS – Templating engine for views

## ⚙️ Getting Started

1. Clone the repo:
   git clone https://github.com/Isha3007/File-Transfer-p2p.git
   cd File-Transfer-p2p

2. Install dependencies:
   npm install

3. Create a `.env` file:
   PORT=
   DATABASE_URL=  
   (Replace with your own MongoDB URL)

4. Run the server:
   node server.js

## 🧪 Usage

- Visit `http://localhost:3000`
- Choose a file and optionally add a password
- Get a unique link to share
- Anyone with the link (and password if added) can download the file

## 🔒 Password Protection

- Passwords are hashed using bcrypt
- Required to download if set during upload
- Secure and never stored in plain text
