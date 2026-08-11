from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(
    title="Backend Development Portfolio",
    description="Student portfolio for backend development assignments",
    version="1.0.0"
)


@app.get("/", response_class=HTMLResponse)
async def portfolio():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <title>Backend Development Portfolio</title>

        <style>
            body {
                font-family: 'Segoe UI', Arial, sans-serif;
                margin: 40px;
                background: #f5f5f5;
            }

            .container {
                max-width: 900px;
                margin: 0 auto;
                background: white;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            }

            h1 {
                color: #2c3e50;
                border-bottom: 3px solid #3498db;
                padding-bottom: 10px;
            }

            .student-info {
                background: #e8f4fd;
                padding: 15px;
                border-radius: 8px;
                margin: 20px 0;
            }

            .student-info strong {
                color: #2c3e50;
            }

            .admission {
                font-size: 1.2em;
                color: #2980b9;
                font-weight: bold;
            }

            .assignment {
                margin: 12px 0;
                padding: 15px;
                background: #f8f9fa;
                border-radius: 8px;
                border-left: 4px solid #3498db;
                transition: all 0.3s ease;
            }

            .assignment:hover {
                background: #e8f4fd;
                transform: translateX(5px);
            }

            .assignment a {
                color: #0366d6;
                text-decoration: none;
                font-weight: 500;
            }

            .assignment a:hover {
                text-decoration: underline;
            }

            .badge {
                display: inline-block;
                background: #3498db;
                color: white;
                padding: 2px 10px;
                border-radius: 12px;
                font-size: 0.8em;
                margin-right: 10px;
            }

            .lesson-topic {
                color: #7f8c8d;
                font-size: 0.9em;
                margin-top: 8px;
            }

            .footer {
                margin-top: 30px;
                text-align: center;
                color: #95a5a6;
                font-size: 0.9em;
                border-top: 1px solid #ecf0f1;
                padding-top: 20px;
            }
        </style>
    </head>

    <body>

        <div class="container">

            <h1>Backend Development Portfolio</h1>

            <div class="student-info">

                <p>
                    <strong>Student Name:</strong>
                    VELMA MAKUBA AMUKONYI
                </p>

                <p class="admission">
                    <strong>Admission Number:</strong>
                    C027-01-0469/2024
                </p>

                <p>
                    <strong>Email:</strong>
                    velma.makuba24@students.dkut.ac.ke
                </p>

            </div>

            <h2>Backend Assignments</h2>

            <p>
                Click on any assignment to view the complete code on GitHub.
            </p>

            <div class="assignment">
                <a href="YOUR_GITHUB_LINK_1" target="_blank">
                    <span class="badge">Lab 1</span>
                    HTTP & Your First API
                </a>
                <div class="lesson-topic">
                    FastAPI + Uvicorn, HTTP Methods, Status Codes
                </div>
            </div>

            <div class="assignment">
                <a href="YOUR_GITHUB_LINK_2" target="_blank">
                    <span class="badge">Lab 2</span>
                    Docker - Packaging Your API
                </a>
                <div class="lesson-topic">
                    Containers, Dockerfiles, Docker Compose
                </div>
            </div>

            <div class="assignment">
                <a href="https://github.com/velmamakuba35-cell/gighub-api" target="_blank">
                    <span class="badge">Lab 3</span>
                    https://github.com/velmamakuba35-cell/gighub-api
                </a>
                <div class="lesson-topic">
                    
                </div>
            </div>

            <div class="assignment">
                <a href="https://github.com/velmamakuba35-cell/library-api" target="_blank">
                    <span class="badge">Lab 4</span>
                    https://github.com/velmamakuba35-cell/library-api
                </a>
                <div class="lesson-topic">
                    
                </div>
            </div>

            <div class="assignment">
                <a href="https://github.com/velmamakuba35-cell/bookstore-api" target="_blank">
                    <span class="badge">Lab 5</span>
                    https://github.com/velmamakuba35-cell/bookstore-api
                </a>
                <div class="lesson-topic">
                
                </div>
            </div>

            <div class="assignment">
                <a href="https://github.com/velmamakuba35-cell/healthtrack-api" target="_blank">
                    <span class="badge">Lab 6</span>
                    https://github.com/velmamakuba35-cell/healthtrack-api
                </a>
                <div class="lesson-topic">
                    
                </div>
            </div>

            <div class="assignment">
                <a href="https://github.com/velmamakuba35-cell/clinicguard-api" target="_blank">
                    <span class="badge">Lesson 7</span>
                    https://github.com/velmamakuba35-cell/clinicguard-api
                </a>
                <div class="lesson-topic">
                    
                </div>
            </div>

            <div class="assignment">
                <a href="https://github.com/velmamakuba35-cell/test-api" target="_blank">
                    <span class="badge">Lab 8</span>
                    https://github.com/velmamakuba35-cell/test-api
                </a>
                <div class="lesson-topic">
                    
                </div>
            </div>

            <div class="assignment">
                <a href="https://github.com/velmamakuba35-cell/sendit-api" target="_blank">
                    <span class="badge">Lab 9</span>
                    https://github.com/velmamakuba35-cell/sendit-api
                </a>
                <div class="lesson-topic">
        
                </div>
            </div>

            <div class="assignment">
                <a href="https://github.com/velmamakuba35-cell/product-api-lab10" target="_blank">
                    <span class="badge">Lab 10</span>
                    https://github.com/velmamakuba35-cell/product-api-lab10
                </a>
                <div class="lesson-topic">
                    
                </div>
            </div>

            <div class="footer">
                Backend Development Portfolio - 2026
            </div>

        </div>

    </body>
    </html>
    """

    return html_content