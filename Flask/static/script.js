function showAlert(message = "This is a sample alert from script.js!") {
  // Check if toast container exists, if not, create it
  if (!document.getElementById('toast-container')) {
    const toastContainer = document.createElement('div');
    toastContainer.id = 'toast-container';
    toastContainer.style.position = 'fixed';
    toastContainer.style.bottom = '30px';
    toastContainer.style.right = '30px';
    toastContainer.style.zIndex = '10000';
    document.body.appendChild(toastContainer);
  }

  // Create toast message
  const toast = document.createElement('div');
  toast.className = 'toast-message';
  toast.innerText = message;

  // Style the toast
  toast.style.background = '#007BFF';
  toast.style.color = '#fff';
  toast.style.padding = '15px 20px';
  toast.style.marginTop = '10px';
  toast.style.borderRadius = '8px';
  toast.style.boxShadow = '0 5px 15px rgba(0,0,0,0.2)';
  toast.style.fontSize = '16px';
  toast.style.opacity = '0';
  toast.style.transition = 'opacity 0.3s ease';

  document.getElementById('toast-container').appendChild(toast);

  // Fade in
  setTimeout(() => {
    toast.style.opacity = '1';
  }, 100);

  // Auto remove after 3 seconds
  setTimeout(() => {
    toast.style.opacity = '0';
    setTimeout(() => {
      toast.remove();
    }, 300);
  }, 3000);
}
