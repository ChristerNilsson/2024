// Generated by CoffeeScript 2.7.0
var NY, XN, XO, YN, YO, drawForm, drawMove, drawTitle, textCol;

XN = 60;

YN = 64;

NY = 40;

XO = 65; // X Offset

YO = 200 - XN; // Y Offset

window.setup = function() {
  var canvas;
  canvas = createCanvas(2100, 2970);
  textAlign(CENTER, CENTER);
  return rectMode(CENTER);
};

// strokeCap PROJECT
drawMove = function(x, y, txt) {
  var i, k, len, ref, results;
  textSize(40);
  ref = range(17);
  results = [];
  for (k = 0, len = ref.length; k < len; k++) {
    i = ref[k];
    fill(i === 2 || i === 3 || i === 6 || i === 7 || i === 10 || i === 11 || i === 14 || i === 15 ? "#eee" : "#fff");
    rect(x + i * XN, y, XN, YN);
    if (i === 0) {
      fill('black');
      results.push(text(txt, x + i * XN, y + 0.1 * YN));
    } else {
      results.push(void 0);
    }
  }
  return results;
};

drawTitle = function(x, y, color) {
  var other;
  fill(color);
  rect(x + 3.5 * XN, y, 8 * XN, 2.8 * YN);
  other = color === 'black' ? 'white' : 'black';
  textSize(32);
  y = y - 0.1 * YN;
  fill(other);
  // text color,x+3.5*XN,y-YN
  text('DT', x, y - YN);
  text('K', x, y - 0.5 * YN);
  text('LS', x, y);
  text('a-h', x + 1 * XN, y);
  text('från', x + 1.5 * XN, y - 0.75 * YN);
  text('1-8', x + 2 * XN, y);
  text('x', x + 3 * XN, y);
  text('DT', x + 4 * XN, y - YN);
  text('LS', x + 4 * XN, y);
  text('a-h', x + 5 * XN, y);
  text('till', x + 5.5 * XN, y - 0.75 * YN);
  text('1-8', x + 6 * XN, y);
  text('DT', x + 7 * XN, y - YN);
  text('†', x + 7 * XN, y - 0.5 * YN);
  return text('LS', x + 7 * XN, y);
};

textCol = function(txt, x, y, w, h, count) {
  fill('black');
  text(txt, x, y - 0.3 * YN);
  noFill();
  rect(x, y + 0.5 * YN, w, h, 5);
  if (count === 2) {
    return rect(x, y + 1.5 * YN, w, h, 5);
  }
};

drawForm = function() {
  var h, i, k, l, len, len1, ref, ref1, t, w, x, y;
  ref = range(4);
  for (k = 0, len = ref.length; k < len; k++) {
    i = ref[k];
    t = "Namn Klubb Rating Poäng".split(" ")[i];
    x = XO + XN * [7.2, 20.6, 29.5, 32.5][i];
    y = YO + NY * YN + 0.2 * XN;
    w = [700, 750, 200, 100][i];
    h = YN;
    textCol(t, x, y, w, h, 2);
  }
  ref1 = range(6);
  for (l = 0, len1 = ref1.length; l < len1; l++) {
    i = ref1[l];
    t = 'Tävling Plats Klass Rond Bord Datum'.split(" ")[i];
    x = XO + XN * [5.3, 13.8, 20.7, 24.6, 27, 30.9][i];
    y = YO + NY * YN + YN * 3;
    w = XN * [8.2, 8, 5, 2, 2, 5][i];
    textCol(t, x, y, w, YN, 1);
  }
  fill('black');
  text('Vit:', XO + XN / 4, YO + NY * YN + 0.7 * YN);
  return text('Svart:', XO + XN / 4, YO + NY * YN + 1.7 * YN);
};

window.mouseClicked = function() {
  return saveCanvas('adam', 'jpg');
};

window.draw = function() {
  var i, j, k, l, len, len1, len2, len3, len4, m, n, o, ref, ref1, ref2, ref3, ref4, results, x, y;
  background('white');
  strokeWeight(1); //100/height
  noFill();
  ref = range(4);
  for (k = 0, len = ref.length; k < len; k++) {
    i = ref[k];
    x = [0, 8 * XN, 17 * XN, 25 * XN][i];
    drawTitle(XO + XN + x, YO - 0.7 * YN, ['white', 'black'][i % 2]);
  }
  drawForm();
  ref1 = range(2);
  for (l = 0, len1 = ref1.length; l < len1; l++) {
    i = ref1[l];
    ref2 = range(NY);
    for (m = 0, len2 = ref2.length; m < len2; m++) {
      j = ref2[m];
      drawMove(XO + i * 17 * XN, YO + j * YN, NY * i + j + 1);
    }
  }
  ref3 = range(5);
  for (n = 0, len3 = ref3.length; n < len3; n++) {
    i = ref3[n];
    strokeWeight([5, 3, 5, 3, 5][i]);
    x = XO + [-0.5, 8.5, 16.5, 25.5, 33.5][i] * XN;
    line(x, YO - YN / 2, x, YO + NY * YN - Math.floor(YN / 2)); // ver
  }
  ref4 = range(5);
  results = [];
  for (o = 0, len4 = ref4.length; o < len4; o++) {
    i = ref4[o];
    strokeWeight([5, 3, 5, 3, 5][i]);
    y = YO + [0, 10, 20, 30, 40][i] * YN - YN / 2;
    results.push(line(XO - 0.5 * XN, y, XO + 33.5 * XN, y)); // hor
  }
  return results;
};

//# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoic2tldGNoLmpzIiwic291cmNlUm9vdCI6Ii4uXFwiLCJzb3VyY2VzIjpbImNvZmZlZVxcc2tldGNoLmNvZmZlZSJdLCJuYW1lcyI6W10sIm1hcHBpbmdzIjoiO0FBQUEsSUFBQSxFQUFBLEVBQUEsRUFBQSxFQUFBLEVBQUEsRUFBQSxFQUFBLEVBQUEsRUFBQSxFQUFBLFFBQUEsRUFBQSxRQUFBLEVBQUEsU0FBQSxFQUFBOztBQUFBLEVBQUEsR0FBSzs7QUFDTCxFQUFBLEdBQUs7O0FBQ0wsRUFBQSxHQUFLOztBQUNMLEVBQUEsR0FBSyxHQUhMOztBQUlBLEVBQUEsR0FBSyxHQUFBLEdBQUksR0FKVDs7QUFNQSxNQUFNLENBQUMsS0FBUCxHQUFlLFFBQUEsQ0FBQSxDQUFBO0FBQ2YsTUFBQTtFQUFDLE1BQUEsR0FBUyxZQUFBLENBQWEsSUFBYixFQUFrQixJQUFsQjtFQUNULFNBQUEsQ0FBVSxNQUFWLEVBQWlCLE1BQWpCO1NBQ0EsUUFBQSxDQUFTLE1BQVQ7QUFIYyxFQU5mOzs7QUFZQSxRQUFBLEdBQVcsUUFBQSxDQUFDLENBQUQsRUFBRyxDQUFILEVBQUssR0FBTCxDQUFBO0FBQ1gsTUFBQSxDQUFBLEVBQUEsQ0FBQSxFQUFBLEdBQUEsRUFBQSxHQUFBLEVBQUE7RUFBQyxRQUFBLENBQVMsRUFBVDtBQUNBO0FBQUE7RUFBQSxLQUFBLHFDQUFBOztJQUNDLElBQUEsQ0FBUSxNQUFNLEtBQU4sTUFBUSxLQUFSLE1BQVUsS0FBVixNQUFZLEtBQVosTUFBYyxNQUFkLE1BQWlCLE1BQWpCLE1BQW9CLE1BQXBCLE1BQXVCLEVBQTFCLEdBQW1DLE1BQW5DLEdBQStDLE1BQXBEO0lBQ0EsSUFBQSxDQUFLLENBQUEsR0FBRSxDQUFBLEdBQUUsRUFBVCxFQUFZLENBQVosRUFBYyxFQUFkLEVBQWlCLEVBQWpCO0lBQ0EsSUFBRyxDQUFBLEtBQUssQ0FBUjtNQUNDLElBQUEsQ0FBSyxPQUFMO21CQUNBLElBQUEsQ0FBSyxHQUFMLEVBQVMsQ0FBQSxHQUFFLENBQUEsR0FBRSxFQUFiLEVBQWdCLENBQUEsR0FBRSxHQUFBLEdBQUksRUFBdEIsR0FGRDtLQUFBLE1BQUE7MkJBQUE7O0VBSEQsQ0FBQTs7QUFGVTs7QUFTWCxTQUFBLEdBQVksUUFBQSxDQUFDLENBQUQsRUFBRyxDQUFILEVBQUssS0FBTCxDQUFBO0FBQ1osTUFBQTtFQUFDLElBQUEsQ0FBSyxLQUFMO0VBQ0EsSUFBQSxDQUFLLENBQUEsR0FBRSxHQUFBLEdBQUksRUFBWCxFQUFjLENBQWQsRUFBZ0IsQ0FBQSxHQUFFLEVBQWxCLEVBQXFCLEdBQUEsR0FBSSxFQUF6QjtFQUVBLEtBQUEsR0FBVyxLQUFBLEtBQU8sT0FBVixHQUF1QixPQUF2QixHQUFvQztFQUM1QyxRQUFBLENBQVMsRUFBVDtFQUNBLENBQUEsR0FBSSxDQUFBLEdBQUksR0FBQSxHQUFJO0VBRVosSUFBQSxDQUFLLEtBQUwsRUFQRDs7RUFTQyxJQUFBLENBQUssSUFBTCxFQUFVLENBQVYsRUFBWSxDQUFBLEdBQUUsRUFBZDtFQUNBLElBQUEsQ0FBSyxHQUFMLEVBQVMsQ0FBVCxFQUFXLENBQUEsR0FBRSxHQUFBLEdBQUksRUFBakI7RUFDQSxJQUFBLENBQUssSUFBTCxFQUFVLENBQVYsRUFBWSxDQUFaO0VBQ0EsSUFBQSxDQUFLLEtBQUwsRUFBVyxDQUFBLEdBQUUsQ0FBQSxHQUFFLEVBQWYsRUFBa0IsQ0FBbEI7RUFDQSxJQUFBLENBQUssTUFBTCxFQUFZLENBQUEsR0FBRSxHQUFBLEdBQUksRUFBbEIsRUFBcUIsQ0FBQSxHQUFFLElBQUEsR0FBSyxFQUE1QjtFQUNBLElBQUEsQ0FBSyxLQUFMLEVBQVcsQ0FBQSxHQUFFLENBQUEsR0FBRSxFQUFmLEVBQWtCLENBQWxCO0VBQ0EsSUFBQSxDQUFLLEdBQUwsRUFBUyxDQUFBLEdBQUUsQ0FBQSxHQUFFLEVBQWIsRUFBZ0IsQ0FBaEI7RUFFQSxJQUFBLENBQUssSUFBTCxFQUFVLENBQUEsR0FBRSxDQUFBLEdBQUUsRUFBZCxFQUFpQixDQUFBLEdBQUUsRUFBbkI7RUFDQSxJQUFBLENBQUssSUFBTCxFQUFVLENBQUEsR0FBRSxDQUFBLEdBQUUsRUFBZCxFQUFpQixDQUFqQjtFQUNBLElBQUEsQ0FBSyxLQUFMLEVBQVcsQ0FBQSxHQUFFLENBQUEsR0FBRSxFQUFmLEVBQWtCLENBQWxCO0VBQ0EsSUFBQSxDQUFLLE1BQUwsRUFBWSxDQUFBLEdBQUUsR0FBQSxHQUFJLEVBQWxCLEVBQXFCLENBQUEsR0FBRSxJQUFBLEdBQUssRUFBNUI7RUFDQSxJQUFBLENBQUssS0FBTCxFQUFXLENBQUEsR0FBRSxDQUFBLEdBQUUsRUFBZixFQUFrQixDQUFsQjtFQUNBLElBQUEsQ0FBSyxJQUFMLEVBQVUsQ0FBQSxHQUFFLENBQUEsR0FBRSxFQUFkLEVBQWlCLENBQUEsR0FBRSxFQUFuQjtFQUNBLElBQUEsQ0FBSyxHQUFMLEVBQVMsQ0FBQSxHQUFFLENBQUEsR0FBRSxFQUFiLEVBQWdCLENBQUEsR0FBRSxHQUFBLEdBQUksRUFBdEI7U0FDQSxJQUFBLENBQUssSUFBTCxFQUFVLENBQUEsR0FBRSxDQUFBLEdBQUUsRUFBZCxFQUFpQixDQUFqQjtBQXpCVzs7QUEyQlosT0FBQSxHQUFVLFFBQUEsQ0FBQyxHQUFELEVBQUssQ0FBTCxFQUFPLENBQVAsRUFBUyxDQUFULEVBQVcsQ0FBWCxFQUFhLEtBQWIsQ0FBQTtFQUNULElBQUEsQ0FBSyxPQUFMO0VBQ0EsSUFBQSxDQUFLLEdBQUwsRUFBUyxDQUFULEVBQVcsQ0FBQSxHQUFFLEdBQUEsR0FBSSxFQUFqQjtFQUNBLE1BQUEsQ0FBQTtFQUNBLElBQUEsQ0FBSyxDQUFMLEVBQU8sQ0FBQSxHQUFFLEdBQUEsR0FBSSxFQUFiLEVBQWdCLENBQWhCLEVBQWtCLENBQWxCLEVBQW9CLENBQXBCO0VBQ0EsSUFBRyxLQUFBLEtBQU8sQ0FBVjtXQUFpQixJQUFBLENBQUssQ0FBTCxFQUFPLENBQUEsR0FBRSxHQUFBLEdBQUksRUFBYixFQUFnQixDQUFoQixFQUFrQixDQUFsQixFQUFvQixDQUFwQixFQUFqQjs7QUFMUzs7QUFPVixRQUFBLEdBQVcsUUFBQSxDQUFBLENBQUE7QUFFWCxNQUFBLENBQUEsRUFBQSxDQUFBLEVBQUEsQ0FBQSxFQUFBLENBQUEsRUFBQSxHQUFBLEVBQUEsSUFBQSxFQUFBLEdBQUEsRUFBQSxJQUFBLEVBQUEsQ0FBQSxFQUFBLENBQUEsRUFBQSxDQUFBLEVBQUE7QUFBQztFQUFBLEtBQUEscUNBQUE7O0lBQ0MsQ0FBQSxHQUFJLHlCQUF5QixDQUFDLEtBQTFCLENBQWdDLEdBQWhDLENBQW9DLENBQUMsQ0FBRDtJQUN4QyxDQUFBLEdBQUksRUFBQSxHQUFLLEVBQUEsR0FBSyxDQUFDLEdBQUQsRUFBSyxJQUFMLEVBQVUsSUFBVixFQUFlLElBQWYsQ0FBb0IsQ0FBQyxDQUFEO0lBQ2xDLENBQUEsR0FBSSxFQUFBLEdBQUssRUFBQSxHQUFLLEVBQVYsR0FBZSxHQUFBLEdBQU07SUFDekIsQ0FBQSxHQUFJLENBQUMsR0FBRCxFQUFLLEdBQUwsRUFBUyxHQUFULEVBQWEsR0FBYixDQUFpQixDQUFDLENBQUQ7SUFDckIsQ0FBQSxHQUFJO0lBQ0osT0FBQSxDQUFRLENBQVIsRUFBVSxDQUFWLEVBQVksQ0FBWixFQUFjLENBQWQsRUFBZ0IsQ0FBaEIsRUFBa0IsQ0FBbEI7RUFORDtBQVFBO0VBQUEsS0FBQSx3Q0FBQTs7SUFDQyxDQUFBLEdBQUkscUNBQXFDLENBQUMsS0FBdEMsQ0FBNEMsR0FBNUMsQ0FBZ0QsQ0FBQyxDQUFEO0lBQ3BELENBQUEsR0FBSSxFQUFBLEdBQUssRUFBQSxHQUFLLENBQUMsR0FBRCxFQUFNLElBQU4sRUFBWSxJQUFaLEVBQWtCLElBQWxCLEVBQXdCLEVBQXhCLEVBQTJCLElBQTNCLENBQWdDLENBQUMsQ0FBRDtJQUM5QyxDQUFBLEdBQUksRUFBQSxHQUFLLEVBQUEsR0FBSyxFQUFWLEdBQWUsRUFBQSxHQUFLO0lBQ3hCLENBQUEsR0FBSSxFQUFBLEdBQUssQ0FBQyxHQUFELEVBQUssQ0FBTCxFQUFPLENBQVAsRUFBUyxDQUFULEVBQVcsQ0FBWCxFQUFhLENBQWIsQ0FBZSxDQUFDLENBQUQ7SUFDeEIsT0FBQSxDQUFRLENBQVIsRUFBVSxDQUFWLEVBQVksQ0FBWixFQUFjLENBQWQsRUFBZ0IsRUFBaEIsRUFBbUIsQ0FBbkI7RUFMRDtFQU9BLElBQUEsQ0FBSyxPQUFMO0VBQ0EsSUFBQSxDQUFLLE1BQUwsRUFBWSxFQUFBLEdBQUcsRUFBQSxHQUFHLENBQWxCLEVBQW9CLEVBQUEsR0FBSyxFQUFBLEdBQUcsRUFBUixHQUFhLEdBQUEsR0FBSSxFQUFyQztTQUNBLElBQUEsQ0FBSyxRQUFMLEVBQWMsRUFBQSxHQUFHLEVBQUEsR0FBRyxDQUFwQixFQUFzQixFQUFBLEdBQUssRUFBQSxHQUFHLEVBQVIsR0FBYSxHQUFBLEdBQUksRUFBdkM7QUFuQlU7O0FBcUJYLE1BQU0sQ0FBQyxZQUFQLEdBQXNCLFFBQUEsQ0FBQSxDQUFBO1NBQ3JCLFVBQUEsQ0FBVyxNQUFYLEVBQWtCLEtBQWxCO0FBRHFCOztBQUd0QixNQUFNLENBQUMsSUFBUCxHQUFjLFFBQUEsQ0FBQSxDQUFBO0FBQ2QsTUFBQSxDQUFBLEVBQUEsQ0FBQSxFQUFBLENBQUEsRUFBQSxDQUFBLEVBQUEsR0FBQSxFQUFBLElBQUEsRUFBQSxJQUFBLEVBQUEsSUFBQSxFQUFBLElBQUEsRUFBQSxDQUFBLEVBQUEsQ0FBQSxFQUFBLENBQUEsRUFBQSxHQUFBLEVBQUEsSUFBQSxFQUFBLElBQUEsRUFBQSxJQUFBLEVBQUEsSUFBQSxFQUFBLE9BQUEsRUFBQSxDQUFBLEVBQUE7RUFBQyxVQUFBLENBQVcsT0FBWDtFQUNBLFlBQUEsQ0FBYSxDQUFiLEVBREQ7RUFFQyxNQUFBLENBQUE7QUFFQTtFQUFBLEtBQUEscUNBQUE7O0lBQ0MsQ0FBQSxHQUFJLENBQUMsQ0FBRCxFQUFHLENBQUEsR0FBRSxFQUFMLEVBQVEsRUFBQSxHQUFHLEVBQVgsRUFBYyxFQUFBLEdBQUcsRUFBakIsQ0FBb0IsQ0FBQyxDQUFEO0lBQ3hCLFNBQUEsQ0FBVSxFQUFBLEdBQUcsRUFBSCxHQUFNLENBQWhCLEVBQW1CLEVBQUEsR0FBRyxHQUFBLEdBQUksRUFBMUIsRUFBNkIsQ0FBQyxPQUFELEVBQVMsT0FBVCxDQUFpQixDQUFDLENBQUEsR0FBRSxDQUFILENBQTlDO0VBRkQ7RUFJQSxRQUFBLENBQUE7QUFFQTtFQUFBLEtBQUEsd0NBQUE7O0FBQ0M7SUFBQSxLQUFBLHdDQUFBOztNQUNDLFFBQUEsQ0FBUyxFQUFBLEdBQUcsQ0FBQSxHQUFFLEVBQUYsR0FBSyxFQUFqQixFQUFxQixFQUFBLEdBQUcsQ0FBQSxHQUFFLEVBQTFCLEVBQTZCLEVBQUEsR0FBRyxDQUFILEdBQUssQ0FBTCxHQUFPLENBQXBDO0lBREQ7RUFERDtBQUlBO0VBQUEsS0FBQSx3Q0FBQTs7SUFDQyxZQUFBLENBQWEsQ0FBQyxDQUFELEVBQUcsQ0FBSCxFQUFLLENBQUwsRUFBTyxDQUFQLEVBQVMsQ0FBVCxDQUFXLENBQUMsQ0FBRCxDQUF4QjtJQUNBLENBQUEsR0FBSSxFQUFBLEdBQUssQ0FBQyxDQUFDLEdBQUYsRUFBTSxHQUFOLEVBQVUsSUFBVixFQUFlLElBQWYsRUFBb0IsSUFBcEIsQ0FBeUIsQ0FBQyxDQUFELENBQXpCLEdBQStCO0lBQ3hDLElBQUEsQ0FBSyxDQUFMLEVBQU8sRUFBQSxHQUFHLEVBQUEsR0FBRyxDQUFiLEVBQWdCLENBQWhCLEVBQWtCLEVBQUEsR0FBRyxFQUFBLEdBQUcsRUFBTixjQUFTLEtBQUksRUFBL0IsRUFIRDtFQUFBO0FBS0E7QUFBQTtFQUFBLEtBQUEsd0NBQUE7O0lBQ0MsWUFBQSxDQUFhLENBQUMsQ0FBRCxFQUFHLENBQUgsRUFBSyxDQUFMLEVBQU8sQ0FBUCxFQUFTLENBQVQsQ0FBVyxDQUFDLENBQUQsQ0FBeEI7SUFDQSxDQUFBLEdBQUksRUFBQSxHQUFLLENBQUMsQ0FBRCxFQUFHLEVBQUgsRUFBTSxFQUFOLEVBQVMsRUFBVCxFQUFZLEVBQVosQ0FBZSxDQUFDLENBQUQsQ0FBZixHQUFxQixFQUExQixHQUErQixFQUFBLEdBQUc7aUJBQ3RDLElBQUEsQ0FBSyxFQUFBLEdBQUcsR0FBQSxHQUFJLEVBQVosRUFBZSxDQUFmLEVBQWtCLEVBQUEsR0FBRyxJQUFBLEdBQUssRUFBMUIsRUFBNkIsQ0FBN0IsR0FIRDtFQUFBLENBQUE7O0FBcEJhIiwic291cmNlc0NvbnRlbnQiOlsiWE4gPSA2MFxyXG5ZTiA9IDY0XHJcbk5ZID0gNDBcclxuWE8gPSA2NSAgICAjIFggT2Zmc2V0XHJcbllPID0gMjAwLVhOICMgWSBPZmZzZXRcclxuXHJcbndpbmRvdy5zZXR1cCA9IC0+XHJcblx0Y2FudmFzID0gY3JlYXRlQ2FudmFzIDIxMDAsMjk3MFxyXG5cdHRleHRBbGlnbiBDRU5URVIsQ0VOVEVSXHJcblx0cmVjdE1vZGUgQ0VOVEVSXHJcblx0IyBzdHJva2VDYXAgUFJPSkVDVFxyXG5cclxuZHJhd01vdmUgPSAoeCx5LHR4dCkgLT5cclxuXHR0ZXh0U2l6ZSA0MFxyXG5cdGZvciBpIGluIHJhbmdlIDE3XHRcdFxyXG5cdFx0ZmlsbCBpZiBpIGluIFsyLDMsNiw3LDEwLDExLDE0LDE1XSB0aGVuIFwiI2VlZVwiIGVsc2UgXCIjZmZmXCJcdFx0XHJcblx0XHRyZWN0IHgraSpYTix5LFhOLFlOXHJcblx0XHRpZiBpID09IDBcclxuXHRcdFx0ZmlsbCAnYmxhY2snXHJcblx0XHRcdHRleHQgdHh0LHgraSpYTix5KzAuMSpZTlxyXG5cclxuZHJhd1RpdGxlID0gKHgseSxjb2xvcikgLT5cclxuXHRmaWxsIGNvbG9yXHJcblx0cmVjdCB4KzMuNSpYTix5LDgqWE4sMi44KllOXHJcblxyXG5cdG90aGVyID0gaWYgY29sb3I9PSdibGFjaycgdGhlbiAnd2hpdGUnIGVsc2UgJ2JsYWNrJ1xyXG5cdHRleHRTaXplIDMyXHJcblx0eSA9IHkgLSAwLjEqWU5cclxuXHJcblx0ZmlsbCBvdGhlclxyXG5cdCMgdGV4dCBjb2xvcix4KzMuNSpYTix5LVlOXHJcblx0dGV4dCAnRFQnLHgseS1ZTlxyXG5cdHRleHQgJ0snLHgseS0wLjUqWU5cclxuXHR0ZXh0ICdMUycseCx5XHJcblx0dGV4dCAnYS1oJyx4KzEqWE4seVxyXG5cdHRleHQgJ2Zyw6VuJyx4KzEuNSpYTix5LTAuNzUqWU5cclxuXHR0ZXh0ICcxLTgnLHgrMipYTix5XHJcblx0dGV4dCAneCcseCszKlhOLHlcclxuXHJcblx0dGV4dCAnRFQnLHgrNCpYTix5LVlOXHJcblx0dGV4dCAnTFMnLHgrNCpYTix5XHJcblx0dGV4dCAnYS1oJyx4KzUqWE4seVxyXG5cdHRleHQgJ3RpbGwnLHgrNS41KlhOLHktMC43NSpZTlxyXG5cdHRleHQgJzEtOCcseCs2KlhOLHlcclxuXHR0ZXh0ICdEVCcseCs3KlhOLHktWU5cclxuXHR0ZXh0ICfigKAnLHgrNypYTix5LTAuNSpZTlxyXG5cdHRleHQgJ0xTJyx4KzcqWE4seVxyXG5cclxudGV4dENvbCA9ICh0eHQseCx5LHcsaCxjb3VudCkgLT5cclxuXHRmaWxsICdibGFjaydcclxuXHR0ZXh0IHR4dCx4LHktMC4zKllOXHJcblx0bm9GaWxsKClcclxuXHRyZWN0IHgseSswLjUqWU4sdyxoLDVcclxuXHRpZiBjb3VudD09MiB0aGVuIHJlY3QgeCx5KzEuNSpZTix3LGgsNVxyXG5cclxuZHJhd0Zvcm0gPSAtPlxyXG5cclxuXHRmb3IgaSBpbiByYW5nZSA0XHJcblx0XHR0ID0gXCJOYW1uIEtsdWJiIFJhdGluZyBQb8OkbmdcIi5zcGxpdChcIiBcIilbaV1cclxuXHRcdHggPSBYTyArIFhOICogWzcuMiwyMC42LDI5LjUsMzIuNV1baV1cclxuXHRcdHkgPSBZTyArIE5ZICogWU4gKyAwLjIgKiBYTlxyXG5cdFx0dyA9IFs3MDAsNzUwLDIwMCwxMDBdW2ldXHJcblx0XHRoID0gWU5cclxuXHRcdHRleHRDb2wgdCx4LHksdyxoLDJcclxuXHJcblx0Zm9yIGkgaW4gcmFuZ2UgNlxyXG5cdFx0dCA9ICdUw6R2bGluZyBQbGF0cyBLbGFzcyBSb25kIEJvcmQgRGF0dW0nLnNwbGl0KFwiIFwiKVtpXVxyXG5cdFx0eCA9IFhPICsgWE4gKiBbNS4zLCAxMy44LCAyMC43LCAyNC42LCAyNywzMC45XVtpXVxyXG5cdFx0eSA9IFlPICsgTlkgKiBZTiArIFlOICogMyBcclxuXHRcdHcgPSBYTiAqIFs4LjIsOCw1LDIsMiw1XVtpXVxyXG5cdFx0dGV4dENvbCB0LHgseSx3LFlOLDFcclxuXHJcblx0ZmlsbCAnYmxhY2snXHJcblx0dGV4dCAnVml0OicsWE8rWE4vNCxZTyArIE5ZKllOICsgMC43KllOXHJcblx0dGV4dCAnU3ZhcnQ6JyxYTytYTi80LFlPICsgTlkqWU4gKyAxLjcqWU5cclxuXHJcbndpbmRvdy5tb3VzZUNsaWNrZWQgPSAtPlxyXG5cdHNhdmVDYW52YXMgJ2FkYW0nLCdqcGcnXHJcblxyXG53aW5kb3cuZHJhdyA9IC0+XHJcblx0YmFja2dyb3VuZCAnd2hpdGUnXHJcblx0c3Ryb2tlV2VpZ2h0IDEgIzEwMC9oZWlnaHRcclxuXHRub0ZpbGwoKVxyXG5cclxuXHRmb3IgaSBpbiByYW5nZSA0XHJcblx0XHR4ID0gWzAsOCpYTiwxNypYTiwyNSpYTl1baV1cclxuXHRcdGRyYXdUaXRsZSBYTytYTit4LCBZTy0wLjcqWU4sWyd3aGl0ZScsJ2JsYWNrJ11baSUyXVxyXG5cclxuXHRkcmF3Rm9ybSgpXHJcblxyXG5cdGZvciBpIGluIHJhbmdlIDJcclxuXHRcdGZvciBqIGluIHJhbmdlIE5ZXHJcblx0XHRcdGRyYXdNb3ZlIFhPK2kqMTcqWE4sIFlPK2oqWU4sTlkqaStqKzFcclxuXHJcblx0Zm9yIGkgaW4gcmFuZ2UgNVxyXG5cdFx0c3Ryb2tlV2VpZ2h0IFs1LDMsNSwzLDVdW2ldXHJcblx0XHR4ID0gWE8gKyBbLTAuNSw4LjUsMTYuNSwyNS41LDMzLjVdW2ldICogWE5cclxuXHRcdGxpbmUgeCxZTy1ZTi8yLCB4LFlPK05ZKllOLVlOLy8yICMgdmVyXHJcblxyXG5cdGZvciBpIGluIHJhbmdlIDVcclxuXHRcdHN0cm9rZVdlaWdodCBbNSwzLDUsMyw1XVtpXVxyXG5cdFx0eSA9IFlPICsgWzAsMTAsMjAsMzAsNDBdW2ldICogWU4gLSBZTi8yXHJcblx0XHRsaW5lIFhPLTAuNSpYTix5LCBYTyszMy41KlhOLHkgIyBob3IiXX0=
//# sourceURL=c:\github\2024\008-Schackprotokoll\coffee\sketch.coffee