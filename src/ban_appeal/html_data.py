def main_page(user):
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>HWHC Ban Appeal System</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                max-width: 800px;
                margin: 0 auto;
                padding: 20px;
                background-color: #1a1a1a;
                color: #e0e0e0;
            }}
            .container {{
                background-color: #2d2d2d;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.3);
            }}
            .step {{
                margin: 20px 0;
                padding: 20px;
                border: 2px solid #444;
                border-radius: 8px;
                position: relative;
                background-color: #333;
            }}
            .step.active {{
                border-color: #5865F2;
            }}
            .step.completed {{
                border-color: #57F287;
                background-color: #1a2f1a;
            }}
            .step-number {{
                position: absolute;
                top: -10px;
                left: 20px;
                background: #2d2d2d;
                padding: 0 10px;
                font-weight: bold;
                color: #5865F2;
            }}
            .step.completed .step-number {{
                color: #57F287;
            }}
            .auth-button {{
                background-color: #5865F2;
                color: white;
                border: none;
                padding: 12px 24px;
                border-radius: 6px;
                font-size: 16px;
                cursor: pointer;
                text-decoration: none;
                display: inline-block;
            }}
            .auth-button:hover {{
                background-color: #4752C4;
            }}
            .auth-button:disabled {{
                background-color: #555;
                cursor: not-allowed;
            }}
            .user-info {{
                display: flex;
                align-items: center;
                gap: 15px;
                margin-top: 10px;
            }}
            .avatar {{
                width: 50px;
                height: 50px;
                border-radius: 50%;
            }}
            .username {{
                font-size: 18px;
                font-weight: bold;
            }}
            .appeal-form {{
                margin-top: 15px;
            }}
            .appeal-textarea {{
                width: 100%;
                min-height: 200px;
                padding: 12px;
                border: 2px solid #555;
                border-radius: 6px;
                font-family: Arial, sans-serif;
                resize: vertical;
                box-sizing: border-box;
                background-color: #444;
                color: #e0e0e0;
            }}
            .char-counter {{
                text-align: right;
                margin-top: 5px;
                color: #aaa;
                font-size: 14px;
            }}
            .char-counter.error {{
                color: #ff6b6b;
            }}
            .submit-button {{
                background-color: #57F287;
                color: white;
                border: none;
                padding: 12px 24px;
                border-radius: 6px;
                font-size: 16px;
                cursor: pointer;
                margin-top: 10px;
            }}
            .submit-button:hover {{
                background-color: #3BA55D;
            }}
            .submit-button:disabled {{
                background-color: #555;
                cursor: not-allowed;
            }}
            h1 {{
                color: #5865F2;
                text-align: center;
                margin-bottom: 30px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>HWHC Ban Appeal System</h1>
            
            <!-- Step 1: Authentication -->
            <div class="step {'completed' if user else 'active'}">
                <div class="step-number">Step 1</div>
                <h3>Authenticate</h3>
                {'<!-- Authenticated User Display -->' if user else '<!-- Not Authenticated Display -->'}
                {f'''
                <div class="user-info">
                    <img src="https://cdn.discordapp.com/avatars/{user['id']}/{user['avatar']}.png" alt="Avatar" class="avatar" onerror="this.src='https://cdn.discordapp.com/embed/avatars/0.png'">
                    <div>
                        <div class="username">{user['username']}</div>
                        <div>Authenticated successfully</div>
                    </div>
                </div>
                <button class="auth-button" disabled>✓ Authenticated with Discord</button>
                ''' if user else '''
                <p>You need to authenticate with Discord to submit a ban appeal. This will only give access to basic account information (username and avatar).</p>
                <a href="/login" class="auth-button">Authenticate with Discord</a>
                '''}
            </div>
            
            <!-- Step 2: Appeal Form -->
            <div class="step {'active' if user else ''}">
                <div class="step-number">Step 2</div>
                <h3>Submit Appeal</h3>
                {'''
                <form class="appeal-form" method="POST" action="/appeal" onsubmit="return validateForm()">
                    <label for="appeal-text">Please explain why you believe your ban should be lifted (100-5000 characters):</label>
                    <textarea 
                        id="appeal-text" 
                        name="appeal_text" 
                        class="appeal-textarea" 
                        placeholder="Enter your ban appeal here... Please be respectful and provide detailed information about your situation."
                        oninput="updateCharCounter()"
                        required
                    ></textarea>
                    <div class="char-counter" id="char-counter">0 / 5000 characters</div>
                    <button type="submit" class="submit-button" id="submit-btn" disabled>Submit Appeal</button>
                </form>
                
                <script>
                    function updateCharCounter() {{
                        const textarea = document.getElementById('appeal-text');
                        const counter = document.getElementById('char-counter');
                        const submitBtn = document.getElementById('submit-btn');
                        const length = textarea.value.length;
                        
                        counter.textContent = length + ' / 5000 characters';
                        
                        if (length < 100 || length > 5000) {{
                            counter.style.color = '#e74c3c';
                            submitBtn.disabled = true;
                            if (length < 100) {{
                                counter.textContent += ' (minimum 100)';
                            }} else {{
                                counter.textContent += ' (maximum 5000)';
                            }}
                        }} else {{
                            counter.style.color = '#27ae60';
                            submitBtn.disabled = false;
                        }}
                    }}
                    
                    function validateForm() {{
                        const textarea = document.getElementById('appeal-text');
                        const length = textarea.value.length;

                        if (length < 100) {{
                            alert('Appeal text must be at least 100 characters long.');
                            return false;
                        }}
                        if (length > 5000) {{
                            alert('Appeal text must be no more than 5000 characters long.');
                            return false;
                        }}
                        
                        return true;
                    }}
                </script>
                ''' if user else '''
                <p>Please authenticate first to submit your ban appeal.</p>
                <textarea 
                    class="appeal-textarea" 
                    placeholder="Please authenticate with Discord first..."
                    disabled
                ></textarea>
                <button class="submit-button" disabled>Submit Appeal</button>
                '''}
            </div>
        </div>
    </body>
    </html>
    """

def FAILED_APPEAL(len_appeal_text):
    return f"""
            <!DOCTYPE html>
            <html>
            <head>
                <title>Appeal Submission Error</title>
                <style>
                    body {{ font-family: Arial, sans-serif; max-width: 600px; margin: 50px auto; padding: 20px; background-color: #1a1a1a; color: #e0e0e0; }}
                    .error {{ background: #2d1a1a; border: 1px solid #ff6b6b; padding: 20px; border-radius: 5px; }}
                    .button {{ background: #5865F2; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px; }}
                </style>
            </head>
            <body>
                <div class="error">
                    <h2>Invalid Appeal Length</h2>
                    <p>Your appeal must be between 100 and 5000 characters. Current length: {len_appeal_text} characters.</p>
                    <a href="/" class="button">Go Back</a>
                </div>
            </body>
            </html>
            """

def SUCCESSFUL_APPEAL(user, appeal_text):
    return f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Appeal Submitted</title>
            <style>
                body {{ 
                    font-family: Arial, sans-serif; 
                    max-width: 600px; 
                    margin: 50px auto; 
                    padding: 20px;
                    background-color: #1a1a1a;
                    color: #e0e0e0;
                }}
                .success {{ 
                    background: #1a2f1a; 
                    border: 2px solid #57F287; 
                    padding: 30px; 
                    border-radius: 10px;
                    text-align: center;
                }}
                .button {{ 
                    background: #5865F2; 
                    color: white; 
                    padding: 12px 24px; 
                    text-decoration: none; 
                    border-radius: 6px;
                    display: inline-block;
                    margin-top: 20px;
                }}
                .button:hover {{ background: #4752C4; }}
                h2 {{ color: #57F287; }}
                .user-info {{ margin: 15px 0; color: #aaa; }}
            </style>
        </head>
        <body>
            <div class="success">
                <h2>✓ Appeal Submitted Successfully!</h2>
                <p>Thank you, <strong>{user['username']}</strong>!</p>
                <p>Your ban appeal has been received and will be reviewed by our moderation team.</p>
                <div class="user-info">
                    <p><strong>Appeal Length:</strong> {len(appeal_text)} characters</p>
                    <p><strong>Submitted:</strong> Just now</p>
                </div>
                <p>You will be contacted via Discord if any additional information is needed.</p>
                <a href="/" class="button">Return to Home</a>
            </div>
        </body>
        </html>
        """