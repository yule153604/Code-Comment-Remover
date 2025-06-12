# app.py
from flask import Flask, render_template, request, flash
import logging

try:
    import pygments
    from pygments.lexers import guess_lexer
    from pygments.token import Comment
    from pygments.util import ClassNotFound
    PYGMENTS_AVAILABLE = True
except ImportError:
     PYGMENTS_AVAILABLE = False
     logging.error("Pygments library not found. Please install it: pip install Pygments")


app = Flask(__name__)
# flash messages need a secret key
app.config['SECRET_KEY'] = 'a-very-secret-key-change-it' 

# Configure logging
logging.basicConfig(level=logging.INFO)

def process_code_with_pygments(code, lexer):
    """
    Iterates through tokens using the given lexer and removes comment tokens.
    """
    if not PYGMENTS_AVAILABLE:
         return code, "Pygments library missing!"
         
    logging.info(f"Processing with lexer: {lexer.name}")
    try:
       # get_tokens returns a generator of (token_type, token_value)
        tokens = lexer.get_tokens(code)
        # Join values only if the token type is NOT a subset of Comment
        cleaned_code = "".join(value for ttype, value in tokens if ttype not in Comment)
        return cleaned_code, None
    except Exception as e:
         logging.error(f"Error during tokenizing with {lexer.name}: {e}")
         return code, f"Error processing code as {lexer.name}: {e}"


@app.route('/', methods=['GET', 'POST'])
def index():
    original_code = ""
    cleaned_code = ""
    detected_language = "Not yet detected / Unknown"
    
    if not PYGMENTS_AVAILABLE:
         flash("Pygments library is not installed. Functionality is disabled.", "error")
         # Still render the page but with the error message
         return render_template('index.html', 
                                original_code=original_code,
                                cleaned_code=cleaned_code,
                                detected_language="Dependency Error")


    if request.method == 'POST':
        original_code = request.form.get('code_input', '')
        
        # Handle empty input
        if not original_code.strip():
             flash("Please enter some code.", "warning")
             return render_template('index.html', 
                                     original_code=original_code,
                                     cleaned_code="",
                                     detected_language="No Input")

        try:
            # 1. Auto-detect language
            # guess_lexer can be inaccurate for very short snippets
            lexer = guess_lexer(original_code)
            detected_language = f"{lexer.name} (Confidence: {lexer.analyse_text(original_code):.2f})"
            logging.info(f"Detected language: {lexer.name}")

            # 2. Remove comments
            cleaned_code, error = process_code_with_pygments(original_code, lexer)
            if error:
                 flash(error, "error")
                 # show original code if processing failed
                 cleaned_code = original_code 
            else:
                 flash(f"Successfully processed as {lexer.name}.", "success")

        except ClassNotFound:
            # guess_lexer raises ClassNotFound if it cannot determine the language
            detected_language = "Unknown / Ambiguous"
            cleaned_code = original_code # Return original code
            flash("Could not confidently detect the language. Code returned unchanged. Try providing a larger or clearer code snippet.", "warning")
        except Exception as e:
             # Catch other unexpected errors
             logging.error(f"Unexpected error: {e}")
             detected_language = "Error"
             cleaned_code = original_code
             flash(f"An unexpected error occurred: {str(e)}", "error")


    # Render template for both GET (initial load) and POST (after processing)
    return render_template('index.html', 
                           original_code=original_code,
                           cleaned_code=cleaned_code,
                           detected_language=detected_language)

if __name__ == '__main__':
    if PYGMENTS_AVAILABLE:
       print("\nStarting Flask app...")
       print("Access at: http://127.0.0.1:5000")
       app.run(debug=True)
    else:
        print("\nCannot start app: Pygments library is not installed.")
        print("Run: pip install Pygments\n")