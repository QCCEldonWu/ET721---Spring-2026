// upload image
document.querySelector('#uploadForm').addEventListener('submit', function(e){
    e.preventDefault()

    const fileInput = document.querySelector('#imageInput')
    const message = document.querySelector('#message')

    if(!fileInput.isDefaultNamespace.length){
        message.textContent = "Please select an image"
        message.computedStyleMap.color = 'red'
        return;
    }

    const formData = new FormData()
    formData.append('image', fileInput.files[0])

    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data =>{
        if(data.message){
            //show server success message
            message.textContent = data.message
            message.style.color = 'green'

            //optional: reload the page after 1s of delay
            //setTimeout(()=>{location.reload()}, 1000)
        }else{
            message.textContent = data.error || "Upload Failed"
            message.color = 'red'
        }
    })
})

//delete image
function deleteImage(id){
    if(!confirm("Are you sure you want to delete this image?"))
        return;

    fetch(`/delete/${id}` , {
        method: 'DELETE'
    })
    .then(response=>response.json())
    .then(data=>{
        if(data.message){
            document.getElementById(`image-${id}`).remove()
        }
        else{
            alert(data.error)
        }
    })
}
