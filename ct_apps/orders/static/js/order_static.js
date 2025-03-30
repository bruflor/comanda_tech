function handleChangeInputValue(inputId, type){
    const element = document.getElementById(inputId)
    if(type === 'add'){
        element.value = Number(element.value) + 1
        console.log('increasing', element.value)
    }
    if(type === 'remove'){
        if(Number(element.value) === 0) return
        element.value = Number(element.value) - 1
        console.log('decreasing', element.value)
    }
}