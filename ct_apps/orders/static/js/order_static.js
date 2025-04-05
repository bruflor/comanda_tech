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
    
    if(type === 'deliver'){
        element.value = "retrieved"
        element.dispatchEvent(new Event("change"))
        console.log('retrieved')
    }

}
