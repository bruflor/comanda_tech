function handleChangeInputValue(inputId, type) {
    const element = document.getElementById(inputId)
    if (type === 'add') {
        element.value = Number(element.value) + 1
        element.dispatchEvent(new Event("change"))
        console.log('increasing', element.value)
    }
    if (type === 'remove') {
        if (Number(element.value) === 0) return
        element.value = Number(element.value) - 1
        element.dispatchEvent(new Event("change"))
        console.log('decreasing', element.value)
    }

    if (type === 'deliver') {
        element.value = "retrieved"
        element.dispatchEvent(new Event("change"))
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

        totalDebit.push(totalPerItem)
        // itemStatus.value = "paid"
        

    }
    console.debug('changing')
    totalToPay.value = totalDebit.reduce((previousValue, currentValue) => {
        return previousValue + currentValue
    }, 0)
    totalToPay.innerHTML = totalToPay.value


    changeInput.value = Number(paidAmount.value) - totalToPay.value
    paidInput.value = totalToPay.value

}
