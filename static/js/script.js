var mySwiper = new Swiper(".swiper-container", {
  direction: "vertical",
  loop: true,
  pagination: ".swiper-pagination",
  grabCursor: true,
  speed: 1000,
  paginationClickable: true,
  parallax: true,
  autoplay: false,
  effect: "slide",
  mousewheelControl: 1
});

// document.getElementById('upload-1').addEventListener('change', function(e) {
//   const file = e.target.files[0];
//   if (file) {
//     const reader = new FileReader();
//     reader.onload = function(event) {
//       const images = document.querySelectorAll('.swiper-slide .uploaded-image');
//       const texts = document.querySelectorAll('.swiper-slide .image-text');
//       images.forEach(img => {
//         img.src = event.target.result;
//         img.style.display = 'block';
//       });
//       texts.forEach(text => text.style.display = 'block');
//     };
//     reader.readAsDataURL(file);
//   }
// });




document.getElementById('upload-1').addEventListener('change', function(e) {
  const file = e.target.files[0];
  if (file) {
      // 显示原始图片在左半部分
      const reader = new FileReader();
      reader.onload = function(event) {
          const leftImages = document.querySelectorAll('.swiper-slide .image-upload-container.left .uploaded-image');
          leftImages.forEach(img => {
              img.src = event.target.result;
              img.style.display = 'block';
          });
      };
      reader.readAsDataURL(file);

      // 将图片发送到服务器进行处理
      const formData = new FormData();
      formData.append('file', file);

      fetch('/upload_image', {
          method: 'POST',
          body: formData
      })
      .then(response => response.blob())
      .then(imageBlob => {
          // 创建一个本地 URL，指向处理后的图片
          const imageObjectURL = URL.createObjectURL(imageBlob);
          document.querySelectorAll('.swiper-slide .image-upload-container.right .uploaded-image').forEach(img => {
              img.src = imageObjectURL;
              img.style.display = 'block';
          });
      })
      .catch(error => console.error('Error:', error));
  }
});



document.getElementById('refresh-tab').addEventListener('click', function(e) {
  e.preventDefault();
  window.location.reload(); // 重新加载页面
});

