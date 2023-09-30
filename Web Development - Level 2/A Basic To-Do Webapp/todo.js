// Once the DOM is loaded
document.addEventListener("DOMContentLoaded", function() {
  // Get form and list elements
  const toDoForm = document.getElementById("toDoFormCSS");
  const toDoList = document.getElementById("toDoListCSS");
  
  // Retrieve from localStorage
  const savedToDos = JSON.parse(localStorage.getItem("toDos")) || [];

  // Function to update local storage and refresh the list
  function updateLocalStorageAndRefresh() {
    localStorage.setItem("toDos", JSON.stringify(savedToDos));
    refreshToDoList();
  }

  // Function to refresh the To-Do list
  function refreshToDoList() {
    toDoList.innerHTML = ""; // Clear the current list
    savedToDos.forEach(todo => {
      const newToDo = document.createElement("li");
      newToDo.textContent = todo.task;
      
      if (todo.isCompleted) {
        newToDo.classList.add("checkedOff");
      }
      
      const removeButton = document.createElement("button");
      removeButton.innerText = "X";
      removeButton.addEventListener("click", function() {
        const taskIndex = savedToDos.findIndex(item => item.task === todo.task);
        if (taskIndex !== -1) {
          savedToDos.splice(taskIndex, 1);
          updateLocalStorageAndRefresh();
        }
      });

      newToDo.appendChild(removeButton);
      toDoList.appendChild(newToDo);
    });
  }

  // Listen for form submission
  toDoForm.addEventListener("submit", function(event) {
    event.preventDefault();
    const taskText = document.getElementById("taskBox").value;
    if (taskText.trim() !== "") {
      savedToDos.push({ task: taskText, isCompleted: false });
      updateLocalStorageAndRefresh();
      toDoForm.reset();
    }
  });

  // Listen for click events in the list
  toDoList.addEventListener("click", function(e) {
    const target = e.target;
    const listItem = target.closest("li");
    if (listItem) {
      const taskText = listItem.textContent;
      const task = savedToDos.find(item => item.task === taskText);
      if (target.tagName.toLowerCase() === "li") {
        task.isCompleted = !task.isCompleted;
        updateLocalStorageAndRefresh();
      }
    }
  });

  // Get the Clear To-Do button
  const clearToDo = document.getElementById("clearToDo");

  // Listen for click on the Clear To-Do button
  clearToDo.addEventListener("click", function() {
    localStorage.clear();
    savedToDos.length = 0;
    refreshToDoList();
  });

  // Initial list refresh
  refreshToDoList();
});
