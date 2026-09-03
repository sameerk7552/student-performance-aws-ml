const form = document.getElementById("predictionForm");

const result = document.getElementById("result");

const score = document.getElementById("score");

const error = document.getElementById("error");

const loading = document.getElementById("loading");

const predictButton = document.getElementById("predictButton");


form.addEventListener("submit", async function(event) {

    event.preventDefault();

    // Hide previous result/error
    result.classList.add("hidden");

    error.classList.add("hidden");

    // Get values from form
    const studyHours = parseFloat(
        document.getElementById("study_hours").value
    );

    const attendance = parseFloat(
        document.getElementById("attendance").value
    );

    const previousScore = parseFloat(
        document.getElementById("previous_score").value
    );

    const assignmentsCompleted = parseInt(
        document.getElementById("assignments_completed").value
    );


    // Show loading
    loading.classList.remove("hidden");

    predictButton.disabled = true;


    try {

        // Send data to FastAPI
        const response = await fetch(
            "http://127.0.0.1:8000/predict",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({

                    study_hours: studyHours,

                    attendance: attendance,

                    previous_score: previousScore,

                    assignments_completed: assignmentsCompleted

                })
            }
        );


        // Check API response
        if (!response.ok) {

            throw new Error(
                "Prediction failed. Please check the FastAPI server."
            );

        }


        // Convert response to JSON
        const data = await response.json();


        // Display prediction
        score.textContent =
            data.predicted_final_score;


        result.classList.remove("hidden");


    } catch (err) {

        error.textContent =
            "❌ " + err.message;

        error.classList.remove("hidden");

    }


    // Hide loading
    loading.classList.add("hidden");

    predictButton.disabled = false;

})