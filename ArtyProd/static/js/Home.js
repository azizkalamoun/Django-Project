const animationConfig = {
  targets: '.anime',
  d: [
    { value: (el) => el.getAttribute('data-morph-to'), duration: (el, i) => 2000 },
    { value: (el) => el.getAttribute('d'), duration: (el, i, l) => 2000 }
  ],
  loop: true,
  easing: 'linear',
  update: () => {
    const el = document.querySelector('#defs');
    el.style.display = 'none';
    void el.offsetWidth; // Use void to prevent unnecessary assignment
    el.style.display = 'block';
  }
};

class Defilee {
  constructor(element) {
    if (!element) {
      return;
    }
    this.element = element;
    this._itemSelector = "." + this._itemClass;
  }

  init() {
    this.addLoop();
  }

  addLoop() {
    const parent = this.element;
    Array.from(this.element.children)
      .reverse()
      .forEach((el) => {
        const clone = el.cloneNode(true);
        clone.classList.add('clone');
        parent.insertBefore(clone, parent.firstChild);
      });
  }
}

const defilee = new Defilee(document.querySelector('#defilee'));
defilee.init();

anime(animationConfig);
