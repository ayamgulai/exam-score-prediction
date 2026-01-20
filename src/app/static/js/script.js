document.getElementById("predictBtn").addEventListener("click", async () => {
    const data = {
        study_hours: parseFloat(document.getElementById("study_hours").value),
        class_attendance: parseFloat(document.getElementById("class_attendance").value),
        sleep_hours: parseFloat(document.getElementById("sleep_hours").value),
        sleep_quality: document.getElementById("sleep_quality").value,
        study_method: document.getElementById("study_method").value,
        facility_rating: document.getElementById("facility_rating").value
    };

    document.getElementById("result").innerText = "Predicting...";

    const response = await fetch("/api/predict", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(data)
    });

    const result = await response.json();

    document.getElementById("result").innerText =
        "Predicted Exam Score: " + result.predicted_exam_score;

    document.getElementById("status").innerText =
        "Predicted Status : " + result.status;
    
    document.getElementById("status").style.color =
        result.status === "Pass" ? "green" : "red";
});