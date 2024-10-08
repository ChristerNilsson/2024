// Generated by CoffeeScript 2.7.0
// Detta program användes när man ska kalibrera fyra hörn
// Avläs koordinaterna med F12
var draw, games, img, mousePressed, points, preload, setup;

img = null;

points = [];

// 0 1
// 3 2
games = {};

games.S5254_1 = {
  white: "Thomas Paulin",
  black: "Christer Nilsson",
  result: "1-0",
  corners: "136 241 3321 247 3322 2165 134 2163",
  klass: 4,
  rond: 5
};

games.e2e4_1 = {
  white: "Thomas Paulin",
  black: "Christer Nilsson",
  result: "1-0",
  corners: "138 241 3323 248 3321 2169 132 2162",
  klass: 4,
  rond: 5
};

preload = function() {
  return img = loadImage('data/5254.jpg');
};

//preload = -> img = loadImage 'data/e2e4.jpg'
setup = function() {
  createCanvas(img.width, img.height);
  noFill();
  fill(0);
  strokeWeight(1);
  textSize(44);
  textAlign(LEFT, TOP);
  return rectMode(CENTER);
};

draw = function() {
  var corners, x0, x1, x2, x3, y0, y1, y2, y3;
  image(img, 0, 0);
  fill(0);
  stroke("white");
  // circle mouseX,mouseY,R
  rect(mouseX - 10, mouseY - 10, 20, 3);
  rect(mouseX - 10, mouseY - 10, 3, 20);
  // fill "white"
  point(mouseX + 10, mouseY + 10);
  fill("black");
  text(points.length, mouseX + 30, mouseY + 30);
  stroke('red');
  fill('red');
  corners = games.S5254_1.corners.split(" ");
  // corners = games.e2e4_1.corners.split " "
  [x0, y0, x1, y1, x2, y2, x3, y3] = corners;
  line(x0, y0, x1, y1);
  line(x1, y1, x2, y2);
  line(x2, y2, x3, y3);
  return line(x3, y3, x0, y0);
};

mousePressed = function() {
  points.push(`${round(mouseX - 10)} ${round(mouseY - 10)}`);
  if (points.length === 4) {
    return console.log(points.join(" "));
  }
};

//# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoibWVhc3VyZS5qcyIsInNvdXJjZVJvb3QiOiIuLlxcIiwic291cmNlcyI6WyJjb2ZmZWVcXG1lYXN1cmUuY29mZmVlIl0sIm5hbWVzIjpbXSwibWFwcGluZ3MiOiI7QUFDNkI7O0FBQUEsSUFBQSxJQUFBLEVBQUEsS0FBQSxFQUFBLEdBQUEsRUFBQSxZQUFBLEVBQUEsTUFBQSxFQUFBLE9BQUEsRUFBQTs7QUFFN0IsR0FBQSxHQUFNOztBQUNOLE1BQUEsR0FBUyxHQUhvQjs7OztBQU83QixLQUFBLEdBQVEsQ0FBQTs7QUFDUixLQUFLLENBQUMsT0FBTixHQUFnQjtFQUFDLEtBQUEsRUFBTSxlQUFQO0VBQXdCLEtBQUEsRUFBTSxrQkFBOUI7RUFBa0QsTUFBQSxFQUFPLEtBQXpEO0VBQWdFLE9BQUEsRUFBUyxxQ0FBekU7RUFBZ0gsS0FBQSxFQUFNLENBQXRIO0VBQXlILElBQUEsRUFBSztBQUE5SDs7QUFDaEIsS0FBSyxDQUFDLE1BQU4sR0FBZTtFQUFDLEtBQUEsRUFBTSxlQUFQO0VBQXdCLEtBQUEsRUFBTSxrQkFBOUI7RUFBa0QsTUFBQSxFQUFPLEtBQXpEO0VBQWdFLE9BQUEsRUFBUyxxQ0FBekU7RUFBZ0gsS0FBQSxFQUFNLENBQXRIO0VBQXlILElBQUEsRUFBSztBQUE5SDs7QUFFZixPQUFBLEdBQVUsUUFBQSxDQUFBLENBQUE7U0FBRyxHQUFBLEdBQU0sU0FBQSxDQUFVLGVBQVY7QUFBVCxFQVhtQjs7O0FBYzdCLEtBQUEsR0FBUSxRQUFBLENBQUEsQ0FBQTtFQUNQLFlBQUEsQ0FBYSxHQUFHLENBQUMsS0FBakIsRUFBd0IsR0FBRyxDQUFDLE1BQTVCO0VBQ0EsTUFBQSxDQUFBO0VBQ0EsSUFBQSxDQUFLLENBQUw7RUFDQSxZQUFBLENBQWEsQ0FBYjtFQUNBLFFBQUEsQ0FBUyxFQUFUO0VBQ0EsU0FBQSxDQUFVLElBQVYsRUFBZSxHQUFmO1NBQ0EsUUFBQSxDQUFTLE1BQVQ7QUFQTzs7QUFTUixJQUFBLEdBQU8sUUFBQSxDQUFBLENBQUE7QUFDUCxNQUFBLE9BQUEsRUFBQSxFQUFBLEVBQUEsRUFBQSxFQUFBLEVBQUEsRUFBQSxFQUFBLEVBQUEsRUFBQSxFQUFBLEVBQUEsRUFBQSxFQUFBLEVBQUE7RUFBQyxLQUFBLENBQU0sR0FBTixFQUFXLENBQVgsRUFBYSxDQUFiO0VBQ0EsSUFBQSxDQUFLLENBQUw7RUFDQSxNQUFBLENBQU8sT0FBUCxFQUZEOztFQUlDLElBQUEsQ0FBSyxNQUFBLEdBQU8sRUFBWixFQUFlLE1BQUEsR0FBTyxFQUF0QixFQUEwQixFQUExQixFQUE2QixDQUE3QjtFQUNBLElBQUEsQ0FBSyxNQUFBLEdBQU8sRUFBWixFQUFlLE1BQUEsR0FBTyxFQUF0QixFQUEwQixDQUExQixFQUE0QixFQUE1QixFQUxEOztFQU9DLEtBQUEsQ0FBTSxNQUFBLEdBQU8sRUFBYixFQUFnQixNQUFBLEdBQU8sRUFBdkI7RUFDQSxJQUFBLENBQUssT0FBTDtFQUNBLElBQUEsQ0FBSyxNQUFNLENBQUMsTUFBWixFQUFtQixNQUFBLEdBQU8sRUFBMUIsRUFBNkIsTUFBQSxHQUFPLEVBQXBDO0VBQ0EsTUFBQSxDQUFPLEtBQVA7RUFDQSxJQUFBLENBQUssS0FBTDtFQUVBLE9BQUEsR0FBVSxLQUFLLENBQUMsT0FBTyxDQUFDLE9BQU8sQ0FBQyxLQUF0QixDQUE0QixHQUE1QixFQWJYOztFQWdCQyxDQUFDLEVBQUQsRUFBSSxFQUFKLEVBQU8sRUFBUCxFQUFVLEVBQVYsRUFBYSxFQUFiLEVBQWdCLEVBQWhCLEVBQW1CLEVBQW5CLEVBQXNCLEVBQXRCLENBQUEsR0FBNEI7RUFDNUIsSUFBQSxDQUFLLEVBQUwsRUFBUSxFQUFSLEVBQVcsRUFBWCxFQUFjLEVBQWQ7RUFDQSxJQUFBLENBQUssRUFBTCxFQUFRLEVBQVIsRUFBVyxFQUFYLEVBQWMsRUFBZDtFQUNBLElBQUEsQ0FBSyxFQUFMLEVBQVEsRUFBUixFQUFXLEVBQVgsRUFBYyxFQUFkO1NBQ0EsSUFBQSxDQUFLLEVBQUwsRUFBUSxFQUFSLEVBQVcsRUFBWCxFQUFjLEVBQWQ7QUFyQk07O0FBdUJQLFlBQUEsR0FBZSxRQUFBLENBQUEsQ0FBQTtFQUNkLE1BQU0sQ0FBQyxJQUFQLENBQVksQ0FBQSxDQUFBLENBQUcsS0FBQSxDQUFNLE1BQUEsR0FBTyxFQUFiLENBQUgsRUFBQSxDQUFBLENBQXVCLEtBQUEsQ0FBTSxNQUFBLEdBQU8sRUFBYixDQUF2QixDQUFBLENBQVo7RUFDQSxJQUFHLE1BQU0sQ0FBQyxNQUFQLEtBQWlCLENBQXBCO1dBQ0MsT0FBTyxDQUFDLEdBQVIsQ0FBWSxNQUFNLENBQUMsSUFBUCxDQUFZLEdBQVosQ0FBWixFQUREOztBQUZjIiwic291cmNlc0NvbnRlbnQiOlsiIyBEZXR0YSBwcm9ncmFtIGFudsOkbmRlcyBuw6RyIG1hbiBza2Ega2FsaWJyZXJhIGZ5cmEgaMO2cm5cclxuIyBBdmzDpHMga29vcmRpbmF0ZXJuYSBtZWQgRjEyXHJcblxyXG5pbWcgPSBudWxsXHJcbnBvaW50cyA9IFtdXHJcblxyXG4jIDAgMVxyXG4jIDMgMlxyXG5nYW1lcyA9IHt9XHJcbmdhbWVzLlM1MjU0XzEgPSB7d2hpdGU6XCJUaG9tYXMgUGF1bGluXCIsIGJsYWNrOlwiQ2hyaXN0ZXIgTmlsc3NvblwiLCByZXN1bHQ6XCIxLTBcIiwgY29ybmVyczogXCIxMzYgMjQxIDMzMjEgMjQ3IDMzMjIgMjE2NSAxMzQgMjE2M1wiLCBrbGFzczo0LCByb25kOjUgfVxyXG5nYW1lcy5lMmU0XzEgPSB7d2hpdGU6XCJUaG9tYXMgUGF1bGluXCIsIGJsYWNrOlwiQ2hyaXN0ZXIgTmlsc3NvblwiLCByZXN1bHQ6XCIxLTBcIiwgY29ybmVyczogXCIxMzggMjQxIDMzMjMgMjQ4IDMzMjEgMjE2OSAxMzIgMjE2MlwiLCBrbGFzczo0LCByb25kOjUgfVxyXG5cclxucHJlbG9hZCA9IC0+IGltZyA9IGxvYWRJbWFnZSAnZGF0YS81MjU0LmpwZydcclxuI3ByZWxvYWQgPSAtPiBpbWcgPSBsb2FkSW1hZ2UgJ2RhdGEvZTJlNC5qcGcnXHJcblxyXG5zZXR1cCA9IC0+XHJcblx0Y3JlYXRlQ2FudmFzIGltZy53aWR0aCwgaW1nLmhlaWdodFxyXG5cdG5vRmlsbCgpXHJcblx0ZmlsbCAwXHJcblx0c3Ryb2tlV2VpZ2h0IDFcclxuXHR0ZXh0U2l6ZSA0NFxyXG5cdHRleHRBbGlnbiBMRUZULFRPUFxyXG5cdHJlY3RNb2RlIENFTlRFUlxyXG5cclxuZHJhdyA9IC0+XHJcblx0aW1hZ2UgaW1nLCAwLDBcclxuXHRmaWxsIDBcclxuXHRzdHJva2UgXCJ3aGl0ZVwiXHJcblx0IyBjaXJjbGUgbW91c2VYLG1vdXNlWSxSXHJcblx0cmVjdCBtb3VzZVgtMTAsbW91c2VZLTEwLCAyMCwzXHJcblx0cmVjdCBtb3VzZVgtMTAsbW91c2VZLTEwLCAzLDIwXHJcblx0IyBmaWxsIFwid2hpdGVcIlxyXG5cdHBvaW50IG1vdXNlWCsxMCxtb3VzZVkrMTBcclxuXHRmaWxsIFwiYmxhY2tcIlxyXG5cdHRleHQgcG9pbnRzLmxlbmd0aCxtb3VzZVgrMzAsbW91c2VZKzMwXHJcblx0c3Ryb2tlICdyZWQnXHJcblx0ZmlsbCAncmVkJ1xyXG5cclxuXHRjb3JuZXJzID0gZ2FtZXMuUzUyNTRfMS5jb3JuZXJzLnNwbGl0IFwiIFwiXHJcblx0IyBjb3JuZXJzID0gZ2FtZXMuZTJlNF8xLmNvcm5lcnMuc3BsaXQgXCIgXCJcclxuXHRcclxuXHRbeDAseTAseDEseTEseDIseTIseDMseTNdID0gY29ybmVyc1xyXG5cdGxpbmUgeDAseTAseDEseTFcclxuXHRsaW5lIHgxLHkxLHgyLHkyXHJcblx0bGluZSB4Mix5Mix4Myx5M1xyXG5cdGxpbmUgeDMseTMseDAseTBcclxuXHJcbm1vdXNlUHJlc3NlZCA9IC0+XHJcblx0cG9pbnRzLnB1c2ggXCIje3JvdW5kKG1vdXNlWC0xMCl9ICN7cm91bmQobW91c2VZLTEwKX1cIlxyXG5cdGlmIHBvaW50cy5sZW5ndGggPT0gNCBcclxuXHRcdGNvbnNvbGUubG9nIHBvaW50cy5qb2luIFwiIFwiXHJcbiJdfQ==
//# sourceURL=c:\github\2024\012-mnist\coffee\measure.coffee