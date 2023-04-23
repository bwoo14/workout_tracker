
document.getElementById("add-exercise").addEventListener("click", function() {
    const exercises = document.getElementById("exercises");
    const newRow = document.createElement("div");
    newRow.classList.add("form-row", "exercise-row");

    const exerciseNameCol = document.createElement("div");
    exerciseNameCol.classList.add("form-group", "col-md-4");

    const exerciseName = document.createElement("select");
    exerciseName.classList.add("form-control");
    exerciseName.name = "exercise_name[]";
    exerciseName.required = true;

    for (const exercise of exercisesList) {
        const option = document.createElement("option");
        option.value = exercise;
        option.text = exercise;
        exerciseName.appendChild(option);
    }

    exerciseNameCol.appendChild(exerciseName);
    newRow.appendChild(exerciseNameCol);

    const repsCol = document.createElement("div");
    repsCol.classList.add("form-group", "col-md-4");

    const reps = document.createElement("input");
    reps.classList.add("form-control");
    reps.type = "number";
    reps.name = "reps[]";
    reps.placeholder = "Reps";
    reps.required = true;

    repsCol.appendChild(reps);
    newRow.appendChild(repsCol);

    const weightCol = document.createElement("div");
    weightCol.classList.add("form-group", "col-md-4");

    const weight = document.createElement("input");
    weight.classList.add("form-control");
    weight.type = "number";
    weight.name = "weight[]";
    weight.placeholder = "Weight";
    weight.required = true;

    weightCol.appendChild(weight);
    newRow.appendChild(weightCol);

    const removeCol = document.createElement("div");
    removeCol.classList.add("form-group", "col-md-4");
    const removeBtn = document.createElement("button");
    removeBtn.classList.add("btn", "btn-danger", "remove-exercise", "ml-2");
    removeBtn.type = "button";
    removeBtn.innerHTML = "&times;";
    removeBtn.title = "Remove Exercise";

    removeBtn.addEventListener("click", function () {
        exercises.removeChild(newRow);
    });

    removeCol.appendChild(removeBtn);
    newRow.appendChild(removeCol);

    exercises.appendChild(newRow);
});
