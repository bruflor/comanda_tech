function handleChangeInputValue(inputId, type) {
    const element = document.getElementById(inputId)
    const btnChangeStatus = document.getElementById(`change-status_${inputId}`)

    if (type === 'add') {
        element.value = "to_pay"
        element.dispatchEvent(new Event("change"))
        btnChangeStatus.onclick = () => {
            handleChangeInputValue(element.id, 'remove')
            calcPay()
        }
        btnChangeStatus.innerText = "Remover"
        btnChangeStatus.classList.add("btn-outline-danger")
        btnChangeStatus.classList.remove("btn-outline-success")
        console.log('to pay')
    }

    if (type === 'remove') {
        element.value = "to_remove"
        element.dispatchEvent(new Event("change"))
        btnChangeStatus.onclick = () => {
            handleChangeInputValue(element.id, 'add')
            calcPay()
        }
        btnChangeStatus.innerText = "Adicionar"
        btnChangeStatus.classList.add("btn-outline-success")
        btnChangeStatus.classList.remove("btn-outline-danger")

        console.log('to remove')
    }

    if (type === 'deliver') {
        element.value = "retrieved"
        element.dispatchEvent(new Event("change"))
        btnChangeStatus.disabled = true
        btnChangeStatus.classList.add("d-none")
        console.log('retrieved')
    }

}

const calcPay = () => {
    const itensToPay = document.querySelectorAll("[data-item_to_pay]")

    const totalToPay = document.querySelector("[data-total_to_pay]")
    const paidInput = document.getElementById('paid')
    const paidAmount = document.getElementById('paid-amount')
    const changeInput = document.getElementById('change')

    const totalDebit = []
    for (let item of itensToPay) {
        const itemAmount = 1
        let itemStatus = item.querySelector('input')
        const itemPrice = Number(item.querySelector("[data-item-price]").innerHTML)
        const totalPerItem = itemAmount * itemPrice

        if (itemStatus.value === "to_pay" ) {
            totalDebit.push(totalPerItem)
        }
        // itemStatus.value = "paid"
        

        console.debug(totalDebit)


    }
    totalToPay.value = totalDebit.reduce((previousValue, currentValue) => {
        return previousValue + currentValue
    }, 0)
    totalToPay.innerHTML = totalToPay.value


    changeInput.value = Number(paidAmount.value) - totalToPay.value
    paidInput.value = totalToPay.value

}
