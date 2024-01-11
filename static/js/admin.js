// Получаем массив кнопок
let arrayBtns = document.querySelectorAll(".delete-product")

// Для каждой кнопки назначаем событие
// При клике на кнопку я буду делать ассинхронный запрос
for (let btn of arrayBtns) {
    // Получаю id товара, которые записан в кнопке с помощью пользовательского атрибута
    let id = btn.dataset.id

    // Добавляю кнопки прослушку события клика на мышь
    btn.addEventListener("click", async () => {
        // async - говорит о том, что функция будет работать с ассинхронным кодом
        // await - ждет пока выполнится запрос и запишет его в переменную
        // await не будет работать, если у функции нету слова async
        let response = await fetch("/deleteProduct", {
            method: "POST",

            // Устанавливаем в заголовках, то что наш запрос будет рабоать в формате JSON
            headers: {
                "Content-Type": "application/json",
                // 'Content-Type': 'application/x-www-form-urlencoded',
            },

            // Передаем серверу id приведенные к формату JSON
            body: JSON.stringify(id)
        })

        // Полученный ответ конвертирую из json в JavaScript массив
        let listProducts = await response.json()

        // Получаем div элемент, где хранится список наших товаров
        let container = document.querySelector("#list-products")

        // Очищаю свой div
        container.innerHTML = ""

        for (let product of listProducts) {
            // Создаю тег p с помощью JavaScript
            let p = document.createElement("p")
            p.innerHTML = `Id: ${ product[0] }; Название: ${ product[1] }; Цена: ${ product[2] }`

            let button = document.createElement("button")
            button.innerHTML = "Удалить запись" // Добавляю что будет написано на кнопке
            button.classList.add("delete-product") // Добавляю кнопке класс
            button.dataset.id = product[0] // Добавляем пользовательский атрибут с id

            container.append(p)
            container.append(button)
        }
    })
}
