const getList = document.querySelector('#get')

fetch("/")
    .then((res) => {
        console.log("Resolved", res);
        return res.json();
    })
    .then((data) => {
        console.log(data)
    })
    .catch((e) => {
        console.log("Error", e)
    })

getList.addEventListener('click', function () {
    console.log('clicked')
})
// async function loadList() {
//     const resopnse = await fetch("/");
//     const tasks = await resopnse.json();
//     console.log(tasks);
//     return tasks;
// }

// getList.addEventListener('click', async function () {
//     console.log("clicked")
//     await loadList()
// })