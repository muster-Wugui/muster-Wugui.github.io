// Click any photo to see it big; click anywhere or hit Esc to close.
(function () {
  var shots = document.querySelectorAll('.shot');
  if (!shots.length) return;

  var box = document.createElement('div');
  box.className = 'lightbox';
  box.innerHTML = '<img alt=""><p class="hint">Click anywhere or press Esc to close</p>';
  document.body.appendChild(box);
  var big = box.querySelector('img');

  shots.forEach(function (shot) {
    shot.addEventListener('click', function () {
      big.src = shot.currentSrc || shot.src;
      big.alt = shot.alt;
      box.classList.add('open');
      document.body.style.overflow = 'hidden';
    });
  });

  function close() {
    box.classList.remove('open');
    document.body.style.overflow = '';
  }
  box.addEventListener('click', close);
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') close();
  });
})();
