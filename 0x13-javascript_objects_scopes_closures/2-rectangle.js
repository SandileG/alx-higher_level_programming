#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    this.width = w;
    this.height = h;
  }
}

function createRectangle (w, h) {
  if (w <= 0 || h <= 0 || isNaN(w) || isNaN(h)) {
    return {};
  }
  return new Rectangle(w, h);
}

module.exports = createRectangle;
