// Generated by CoffeeScript 2.7.0
var N, NY, XO, YO, drawForm, drawMove, drawTitle, textCol;

N = 64;

NY = 40;

XO = 120; // X Offset

YO = 200 - N; // Y Offset


// Array.prototype.clear = -> @length = 0
window.setup = function() {
  var canvas;
  canvas = createCanvas(2100, 2970);
  textAlign(CENTER, CENTER);
  rectMode(CENTER);
  return strokeCap(SQUARE);
};

drawMove = function(x, y, txt) {
  var i, k, len, ref, results;
  textSize(40);
  ref = range(15);
  results = [];
  for (k = 0, len = ref.length; k < len; k++) {
    i = ref[k];
    fill(i === 2 || i === 3 || i === 6 || i === 7 || i === 9 || i === 10 || i === 13 || i === 14 ? "#eee" : "#fff");
    rect(x + i * N, y, N, N);
    if (i === 0) {
      fill('black');
    } else {
      noFill();
    }
    results.push(text(txt, x + i * N, y + 0.1 * N));
  }
  return results;
};

drawTitle = function(x, y, color) {
  fill('black');
  textSize(32);
  y = y - 0.1 * N;
  text(color, x + 3 * N, y - N);
  text('KQR', x, y - N / 2);
  text('BN', x, y);
  text('a-h', x + 1 * N, y);
  text('from', x + 1.5 * N, y - N / 2);
  text('1-8', x + 2 * N, y);
  text('x', x + 3 * N, y);
  text('QR', x + 4 * N, y - N / 2);
  text('BN', x + 4 * N, y);
  text('a-h', x + 5 * N, y);
  text('to', x + 5.5 * N, y - N / 2);
  return text('1-8', x + 6 * N, y);
};

textCol = function(txt, x, y, w, h, count) {
  fill('black');
  text(txt, x, y - 0.2 * N);
  noFill();
  rect(x, y + 0.5 * N, w, h);
  if (count === 2) {
    return rect(x, y + 1.5 * N, w, h);
  }
};

drawForm = function() {
  textCol('Name', XO + 6.7 * N, YO + NY * N + 0.2 * N, 700, N, 2);
  textCol('Club', XO + 17.3 * N, YO + NY * N + 0.2 * N, 600, N, 2);
  textCol('Rating', XO + 25 * N, YO + NY * N + 0.2 * N, 200, N, 2);
  textCol('Result', XO + 28.5 * N, YO + NY * N + 0.2 * N, 100, N, 2);
  textCol('Competiton', XO + 2 * N, YO + NY * N + 3 * N, 5 * N, N, 1);
  textCol('Location', XO + 7 * N, YO + NY * N + 3 * N, 5 * N, N, 1);
  textCol('Date', XO + 12 * N, YO + NY * N + 3 * N, 5 * N, N, 1);
  textCol('Series', XO + 17 * N, YO + NY * N + 3 * N, 5 * N, N, 1);
  textCol('Round', XO + 22 * N, YO + NY * N + 3 * N, 5 * N, N, 1);
  textCol('Table', XO + 27 * N, YO + NY * N + 3 * N, 5 * N, N, 1);
  fill('black');
  text('White:', XO, YO + NY * N + 0.7 * N);
  return text('Black:', XO, YO + NY * N + 1.7 * N);
};

window.mouseClicked = function() {
  return saveCanvas('adam', 'jpg');
};

window.draw = function() {
  var i, j, k, l, len, len1, len2, m, ref, ref1, ref2, x;
  background('white');
  strokeWeight(1); //100/height
  noFill();
  ref = range(4);
  for (k = 0, len = ref.length; k < len; k++) {
    i = ref[k];
    x = [0, 7 * N, 15 * N, 22 * N][i];
    drawTitle(XO + N + x, YO - 0.7 * N, ['White', 'Black'][i % 2]);
  }
  drawForm();
  ref1 = range(2);
  for (l = 0, len1 = ref1.length; l < len1; l++) {
    i = ref1[l];
    ref2 = range(NY);
    for (m = 0, len2 = ref2.length; m < len2; m++) {
      j = ref2[m];
      drawMove(XO + i * 15 * N, YO + j * N, NY * i + j + 1);
    }
  }
  strokeWeight(3);
  line(XO + 7.5 * N, YO - N / 2, XO + 7.5 * N, YO + NY * N - Math.floor(N / 2));
  line(XO + 22.5 * N, YO - N / 2, XO + 22.5 * N, YO + NY * N - Math.floor(N / 2));
  strokeWeight(5);
  return line(XO + 14.5 * N, YO - N / 2, XO + 14.5 * N, YO + NY * N - Math.floor(N / 2));
};

//# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoic2tldGNoLmpzIiwic291cmNlUm9vdCI6Ii4uXFwiLCJzb3VyY2VzIjpbImNvZmZlZVxcc2tldGNoLmNvZmZlZSJdLCJuYW1lcyI6W10sIm1hcHBpbmdzIjoiO0FBQUEsSUFBQSxDQUFBLEVBQUEsRUFBQSxFQUFBLEVBQUEsRUFBQSxFQUFBLEVBQUEsUUFBQSxFQUFBLFFBQUEsRUFBQSxTQUFBLEVBQUE7O0FBQUEsQ0FBQSxHQUFJOztBQUNKLEVBQUEsR0FBSzs7QUFDTCxFQUFBLEdBQUssSUFGTDs7QUFHQSxFQUFBLEdBQUssR0FBQSxHQUFJLEVBSFQ7Ozs7QUFPQSxNQUFNLENBQUMsS0FBUCxHQUFlLFFBQUEsQ0FBQSxDQUFBO0FBQ2YsTUFBQTtFQUFDLE1BQUEsR0FBUyxZQUFBLENBQWEsSUFBYixFQUFrQixJQUFsQjtFQUNULFNBQUEsQ0FBVSxNQUFWLEVBQWlCLE1BQWpCO0VBQ0EsUUFBQSxDQUFTLE1BQVQ7U0FDQSxTQUFBLENBQVUsTUFBVjtBQUpjOztBQU1mLFFBQUEsR0FBVyxRQUFBLENBQUMsQ0FBRCxFQUFHLENBQUgsRUFBSyxHQUFMLENBQUE7QUFDWCxNQUFBLENBQUEsRUFBQSxDQUFBLEVBQUEsR0FBQSxFQUFBLEdBQUEsRUFBQTtFQUFDLFFBQUEsQ0FBUyxFQUFUO0FBQ0E7QUFBQTtFQUFBLEtBQUEscUNBQUE7O0lBQ0MsSUFBQSxDQUFRLE1BQU0sS0FBTixNQUFRLEtBQVIsTUFBVSxLQUFWLE1BQVksS0FBWixNQUFjLEtBQWQsTUFBZ0IsTUFBaEIsTUFBbUIsTUFBbkIsTUFBc0IsRUFBekIsR0FBa0MsTUFBbEMsR0FBOEMsTUFBbkQ7SUFDQSxJQUFBLENBQUssQ0FBQSxHQUFFLENBQUEsR0FBRSxDQUFULEVBQVcsQ0FBWCxFQUFhLENBQWIsRUFBZSxDQUFmO0lBQ0EsSUFBRyxDQUFBLEtBQUcsQ0FBTjtNQUFhLElBQUEsQ0FBSyxPQUFMLEVBQWI7S0FBQSxNQUFBO01BQStCLE1BQUEsQ0FBQSxFQUEvQjs7aUJBQ0EsSUFBQSxDQUFLLEdBQUws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SCxDQUE1QztFQUZEO0VBSUEsUUFBQSxDQUFBO0FBRUE7RUFBQSxLQUFBLHdDQUFBOztBQUNDO0lBQUEsS0FBQSx3Q0FBQTs7TUFDQyxRQUFBLENBQVMsRUFBQSxHQUFHLENBQUEsR0FBRSxFQUFGLEdBQUssQ0FBakIsRUFBb0IsRUFBQSxHQUFHLENBQUEsR0FBRSxDQUF6QixFQUEyQixFQUFBLEdBQUcsQ0FBSCxHQUFLLENBQUwsR0FBTyxDQUFsQztJQUREO0VBREQ7RUFJQSxZQUFBLENBQWEsQ0FBYjtFQUNBLElBQUEsQ0FBSyxFQUFBLEdBQUcsR0FBQSxHQUFJLENBQVosRUFBYyxFQUFBLEdBQUcsQ0FBQSxHQUFFLENBQW5CLEVBQXFCLEVBQUEsR0FBRyxHQUFBLEdBQUksQ0FBNUIsRUFBOEIsRUFBQSxHQUFHLEVBQUEsR0FBRyxDQUFOLGNBQVEsSUFBRyxFQUF6QztFQUNBLElBQUEsQ0FBSyxFQUFBLEdBQUcsSUFBQSxHQUFLLENBQWIsRUFBZSxFQUFBLEdBQUcsQ0FBQSxHQUFFLENBQXBCLEVBQXNCLEVBQUEsR0FBRyxJQUFBLEdBQUssQ0FBOUIsRUFBZ0MsRUFBQSxHQUFHLEVBQUEsR0FBRyxDQUFOLGNBQVEsSUFBRyxFQUEzQztFQUNBLFlBQUEsQ0FBYSxDQUFiO1NBQ0EsSUFBQSxDQUFLLEVBQUEsR0FBRyxJQUFBLEdBQUssQ0FBYixFQUFlLEVBQUEsR0FBRyxDQUFBLEdBQUUsQ0FBcEIsRUFBc0IsRUFBQSxHQUFHLElBQUEsR0FBSyxDQUE5QixFQUFnQyxFQUFBLEdBQUcsRUFBQSxHQUFHLENBQU4sY0FBUSxJQUFHLEVBQTNDO0FBbkJhIiwic291cmNlc0NvbnRlbnQiOlsiTiA9IDY0XHJcbk5ZID0gNDBcclxuWE8gPSAxMjAgIyBYIE9mZnNldFxyXG5ZTyA9IDIwMC1OICMgWSBPZmZzZXRcclxuXHJcbiMgQXJyYXkucHJvdG90eXBlLmNsZWFyID0gLT4gQGxlbmd0aCA9IDBcclxuXHJcbndpbmRvdy5zZXR1cCA9IC0+XHJcblx0Y2FudmFzID0gY3JlYXRlQ2FudmFzIDIxMDAsMjk3MFxyXG5cdHRleHRBbGlnbiBDRU5URVIsQ0VOVEVSXHJcblx0cmVjdE1vZGUgQ0VOVEVSXHJcblx0c3Ryb2tlQ2FwIFNRVUFSRVxyXG5cclxuZHJhd01vdmUgPSAoeCx5LHR4dCkgLT5cclxuXHR0ZXh0U2l6ZSA0MFxyXG5cdGZvciBpIGluIHJhbmdlIDE1XHRcdFxyXG5cdFx0ZmlsbCBpZiBpIGluIFsyLDMsNiw3LDksMTAsMTMsMTRdIHRoZW4gXCIjZWVlXCIgZWxzZSBcIiNmZmZcIlx0XHRcclxuXHRcdHJlY3QgeCtpKk4seSxOLE5cclxuXHRcdGlmIGk9PTAgdGhlbiBmaWxsICdibGFjaycgZWxzZSBub0ZpbGwoKVxyXG5cdFx0dGV4dCB0eHQseCtpKk4seSswLjEqTlxyXG5cclxuZHJhd1RpdGxlID0gKHgseSxjb2xvcikgLT5cclxuXHRmaWxsICdibGFjaydcclxuXHR0ZXh0U2l6ZSAzMlxyXG5cdHkgPSB5IC0gMC4xKk5cclxuXHJcblx0dGV4dCBjb2xvcix4KzMqTix5LU5cclxuXHR0ZXh0ICdLUVInLHgseS1OLzJcclxuXHR0ZXh0ICdCTicseCx5XHJcblx0dGV4dCAnYS1oJyx4KzEqTix5XHJcblx0dGV4dCAnZnJvbScseCsxLjUqTix5LU4vMlxyXG5cdHRleHQgJzEtOCcseCsyKk4seVxyXG5cdHRleHQgJ3gnLHgrMypOLHlcclxuXHJcblx0dGV4dCAnUVInLHgrNCpOLHktTi8yXHJcblx0dGV4dCAnQk4nLHgrNCpOLHlcclxuXHR0ZXh0ICdhLWgnLHgrNSpOLHlcclxuXHR0ZXh0ICd0bycseCs1LjUqTix5LU4vMlxyXG5cdHRleHQgJzEtOCcseCs2Kk4seVxyXG5cclxudGV4dENvbCA9ICh0eHQseCx5LHcsaCxjb3VudCkgLT5cclxuXHRmaWxsICdibGFjaydcclxuXHR0ZXh0IHR4dCx4LHktMC4yKk5cclxuXHRub0ZpbGwoKVxyXG5cdHJlY3QgeCx5KzAuNSpOLHcsaFxyXG5cdGlmIGNvdW50PT0yIHRoZW4gcmVjdCB4LHkrMS41Kk4sdyxoXHJcblxyXG5kcmF3Rm9ybSA9IC0+XHJcblx0dGV4dENvbCAnTmFtZScsICBYTys2LjcqTixZTyArIE5ZKk4rMC4yKk4sIDcwMCxOLDJcclxuXHR0ZXh0Q29sICdDbHViJywgIFhPKzE3LjMqTixZTyArIE5ZKk4rMC4yKk4sIDYwMCxOLDJcclxuXHR0ZXh0Q29sICdSYXRpbmcnLFhPKzI1Kk4sWU8gKyBOWSpOKzAuMipOLCAyMDAsTiwyXHJcblx0dGV4dENvbCAnUmVzdWx0JyxYTysyOC41Kk4sWU8gKyBOWSpOKzAuMipOLCAxMDAsTiwyXHJcblxyXG5cdHRleHRDb2wgJ0NvbXBldGl0b24nLFhPKzIqTiwgWU8gKyBOWSpOKzMqTiwgNSpOLE4sMVxyXG5cdHRleHRDb2wgJ0xvY2F0aW9uJywgIFhPKzcqTixZTyArIE5ZKk4rMypOLCA1Kk4sTiwxXHJcblx0dGV4dENvbCAnRGF0ZScsICAgICAgWE8rMTIqTiwgIFlPICsgTlkqTiszKk4sIDUqTixOLDFcclxuXHR0ZXh0Q29sICdTZXJpZXMnLCAgICBYTysxNypOLFlPICsgTlkqTiszKk4sIDUqTixOLDFcclxuXHR0ZXh0Q29sICdSb3VuZCcsICAgICBYTysyMipOLFlPICsgTlkqTiszKk4sIDUqTixOLDFcclxuXHR0ZXh0Q29sICdUYWJsZScsICAgICBYTysyNypOLFlPICsgTlkqTiszKk4sIDUqTixOLDFcclxuXHJcblx0ZmlsbCAnYmxhY2snXHJcblx0dGV4dCAnV2hpdGU6JyxYTyxZTyArIE5ZKk4gKyAwLjcqTlxyXG5cdHRleHQgJ0JsYWNrOicsWE8sWU8gKyBOWSpOICsgMS43Kk5cclxuXHJcblxyXG5cclxud2luZG93Lm1vdXNlQ2xpY2tlZCA9IC0+XHJcblx0c2F2ZUNhbnZhcyAnYWRhbScsJ2pwZydcclxuXHJcbndpbmRvdy5kcmF3ID0gLT5cclxuXHRiYWNrZ3JvdW5kICd3aGl0ZSdcclxuXHRzdHJva2VXZWlnaHQgMSAjMTAwL2hlaWdodFxyXG5cdG5vRmlsbCgpXHJcblxyXG5cdGZvciBpIGluIHJhbmdlIDRcclxuXHRcdHggPSBbMCw3Kk4sMTUqTiwyMipOXVtpXVxyXG5cdFx0ZHJhd1RpdGxlIFhPK04reCwgWU8tMC43Kk4sWydXaGl0ZScsJ0JsYWNrJ11baSUyXVxyXG5cclxuXHRkcmF3Rm9ybSgpXHJcblxyXG5cdGZvciBpIGluIHJhbmdlIDJcclxuXHRcdGZvciBqIGluIHJhbmdlIE5ZXHJcblx0XHRcdGRyYXdNb3ZlIFhPK2kqMTUqTiwgWU8raipOLE5ZKmkraisxXHJcblxyXG5cdHN0cm9rZVdlaWdodCAzXHJcblx0bGluZSBYTys3LjUqTixZTy1OLzIsWE8rNy41Kk4sWU8rTlkqTi1OLy8yXHJcblx0bGluZSBYTysyMi41Kk4sWU8tTi8yLFhPKzIyLjUqTixZTytOWSpOLU4vLzJcclxuXHRzdHJva2VXZWlnaHQgNVxyXG5cdGxpbmUgWE8rMTQuNSpOLFlPLU4vMixYTysxNC41Kk4sWU8rTlkqTi1OLy8yXHJcblxyXG4iXX0=
//# sourceURL=c:\github\2024\008-Berger\coffee\sketch.coffee