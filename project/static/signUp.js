// console.log("hello");
        const imageInput = document.getElementById('image_input');
        const previewImage = document.getElementById('profile_img');
        function previewSelectedImage() {
            const file = imageInput.files[0];
            if (file) {
                const reader = new FileReader();
                reader.readAsDataURL(file);
                reader.onload = function(e) {
                    previewImage.src = e.target.result;
                }
            }
            // console.log(imageInput.value);
        }
        imageInput.addEventListener('change', previewSelectedImage);