let getList = document.querySelector('#get')
let addToList = document.querySelector('#submit')
let clear = document.querySelector('#clear')
const form = document.querySelector('#taskForm')

// this code runs to return and display list of tasks in JSON.
if (getList) {
    getList.addEventListener('click', function () {
        fetch("http://127.0.0.1:5000/get")
            .then((res) => {
                console.log("Resolved", res);
                return res.json();
            })
            .then((data) => {
                console.log("Data: " + data)
                document.getElementById("list").innerHTML = JSON.stringify(data)
                console.log(data)
            })
            .catch((e) => {
                document.getElementById("list").innerHTML = e
                console.log("Error", e)
            })
    })
}
// this runs on get page if display is cleared.
if (clear) {
    clear.addEventListener('click', function () {
        document.getElementById("list").innerHTML = ""
    })
}

if (addToList) {
    addToList.addEventListener('click', function (event) {
        event.preventDefault()
        fetch("http://127.0.0.1:5000/new")
            .then((res) => {
                console.log("Resolved", res);
                return res.json()
            })
            .then((data) => {
                let numToDos = Object.keys(data).length
                const formData = new FormData(form)
                let newTask = formData.get('todo')
                let newStartDate = formData.get('start')
                let newDueDate = formData.get('due')
                data[numToDos] = { due_date: newDueDate, start_date: newStartDate, todo: newTask }
                let updatedList = JSON.stringify(data)
                console.log("Data: " + updatedList)
                return updatedList
            })
            .then((updatedList) => {
                document.getElementById('list').innerHTML = updatedList
            })
            .catch((e) => {
                console.log("oops - something went wrong", e)
            })
    })
}
