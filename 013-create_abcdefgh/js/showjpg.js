// Generated by CoffeeScript 2.7.0
var N, col, draw, echo, img, keyPressed, preload, range, row, ruta, setup;

echo = console.log;

range = _.range;

img = null;

ruta = null;

row = 0;

col = 0;

N = 30;

preload = function() {
  return img = loadImage("Te2e4.jpg");
};

setup = function() {
  createCanvas(img.width, img.height);
  noFill();
  textSize(36);
  fill(0);
  ruta = img.get(N * col, N * row, N, N);
  return ruta.loadPixels();
};

// facit = """d2d4 g7g6
// c1f4 f8g7
// e2e3 g8f6
// b1d2 e878
// g1f3 d7d6
// f1d3 b7b6
// h2h3 c8b7
// g2g4 f6d5
// f4g3 d5b4
// d3e2 b8d7
// c2c3 b4c6
// h3h4 d7f6
// g4g5 f6d7
// h4h5 e7e6
// h5g6 f7g6
// e3e4 d6d5
// b2b4 d5e4
// d2e4 c6d4
// f3d4 b7e4
// d4e6 g7c3
// e1f1 d8e7
// e6f8 18f8
// a1c1 e4h1
// d1b3 g8h8
// b3c3 e8g8
// c3c7 h1e4
// e2g4 e4f5
// g4e2 f583
// f1e1 f8f5
// c1d1 f5g5
// c7d8 g7f8
// d8g5 f8b4
// d1d2 b4b1
// e2d1 b1e4
// d2e2 e4h1
// e1d2 h1c6
// e2e8 h8g7
// g5e7 g7h6
// g3f4"""
keyPressed = function() {
  if (key === 'ArrowRight') {
    col += 1;
  }
  if (key === 'ArrowLeft') {
    col -= 1;
  }
  if (key === 'ArrowDown') {
    row += 1;
  }
  if (key === 'ArrowUp') {
    row -= 1;
  }
  // if key == ' '
  // 	lines = []
  // 	for drag in range 39
  // 	    for ix in [1,6,12,17]
  // 	        letter = facit[drag][ix]
  //             if letter not in "abcdefgh" then continue
  //             row = drag % 20
  //             coloffset = 2 * (drag // 20)
  //             col = ix % 2 + coloffset
  //             index = row * 33 + [1,6,12,17][col]

  //             facitRuta = letter

  //         if facitRuta in "abcdefgh"
  //             ruta = img.get N*col,N*row,N,N
  //             ruta.loadPixels()
  //             rad = [{a:"36", b:"37",c:'38', d:"39",e:"40", f:"41",g:'42', h:"43"}[facitRuta]]
  //             for i in range 1,29
  //                 for j in range 1,29
  //                     index = N * j + i
  //                     rad.push str 255 - ruta.pixels[4*index]
  //             print rad.length
  //             lines.push rad.join(",")
  // 	saveStrings lines,'Te2e4','csv'
  // 	row = 0
  // 	col = 0
  // else
  // fetch 28x28 matrix
  ruta = img.get(N * col, N * row, N, N);
  return ruta.loadPixels();
};

// echo ruta.pixels
draw = function() {
  var i, index, j, k, len, ref, results, small, xa, xb, ya, yb;
  background("gray");
  image(img, 0, 0);
  fill('red');
  stroke('red');
  small = [];
  fill('red');
  xa = round(lerp(0, 33 * N, col / 33));
  ya = round(lerp(0, 20 * N, row / 20));
  xb = round(lerp(0, 33 * N, (col + 1) / 33));
  yb = round(lerp(0, 20 * N, (row + 1) / 20));
  line(xa, ya, xb, ya);
  line(xb, ya, xb, yb);
  line(xa, yb, xb, yb);
  line(xa, ya, xa, yb);
  fill(255);
  rect(620, 280, 280, 280);
  noStroke();
  if (ruta.pixels) {
    ref = range(28);
    results = [];
    for (k = 0, len = ref.length; k < len; k++) {
      i = ref[k];
      results.push((function() {
        var l, len1, ref1, results1;
        ref1 = range(28);
        results1 = [];
        for (l = 0, len1 = ref1.length; l < len1; l++) {
          j = ref1[l];
          index = N * j + i;
          fill(ruta.pixels[4 * index]);
          results1.push(circle(620 + i * 10, 280 + j * 10, 10));
        }
        return results1;
      })());
    }
    return results;
  }
};

//# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoic2hvd2pwZy5qcyIsInNvdXJjZVJvb3QiOiIuLlxcIiwic291cmNlcyI6WyJjb2ZmZWVcXHNob3dqcGcuY29mZmVlIl0sIm5hbWVzIjpbXSwibWFwcGluZ3MiOiI7QUFBQSxJQUFBLENBQUEsRUFBQSxHQUFBLEVBQUEsSUFBQSxFQUFBLElBQUEsRUFBQSxHQUFBLEVBQUEsVUFBQSxFQUFBLE9BQUEsRUFBQSxLQUFBLEVBQUEsR0FBQSxFQUFBLElBQUEsRUFBQTs7QUFBQSxJQUFBLEdBQU8sT0FBTyxDQUFDOztBQUNmLEtBQUEsR0FBUSxDQUFDLENBQUM7O0FBRVYsR0FBQSxHQUFNOztBQUNOLElBQUEsR0FBTzs7QUFFUCxHQUFBLEdBQU07O0FBQ04sR0FBQSxHQUFNOztBQUVOLENBQUEsR0FBSTs7QUFFSixPQUFBLEdBQVUsUUFBQSxDQUFBLENBQUE7U0FDVCxHQUFBLEdBQU0sU0FBQSxDQUFVLFdBQVY7QUFERzs7QUFHVixLQUFBLEdBQVEsUUFBQSxDQUFBLENBQUE7RUFDUCxZQUFBLENBQWEsR0FBRyxDQUFDLEtBQWpCLEVBQXVCLEdBQUcsQ0FBQyxNQUEzQjtFQUNBLE1BQUEsQ0FBQTtFQUNBLFFBQUEsQ0FBUyxFQUFUO0VBQ0EsSUFBQSxDQUFLLENBQUw7RUFFQSxJQUFBLEdBQU8sR0FBRyxDQUFDLEdBQUosQ0FBUSxDQUFBLEdBQUUsR0FBVixFQUFjLENBQUEsR0FBRSxHQUFoQixFQUFvQixDQUFwQixFQUFzQixDQUF0QjtTQUNQLElBQUksQ0FBQyxVQUFMLENBQUE7QUFQTyxFQWRSOzs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7OztBQStEQSxVQUFBLEdBQWEsUUFBQSxDQUFBLENBQUE7RUFDWixJQUFHLEdBQUEsS0FBTyxZQUFWO0lBQTRCLEdBQUEsSUFBTyxFQUFuQzs7RUFDQSxJQUFHLEdBQUEsS0FBTyxXQUFWO0lBQTJCLEdBQUEsSUFBTyxFQUFsQzs7RUFDQSxJQUFHLEdBQUEsS0FBTyxXQUFWO0lBQTJCLEdBQUEsSUFBTyxFQUFsQzs7RUFDQSxJQUFHLEdBQUEsS0FBTyxTQUFWO0lBQXlCLEdBQUEsSUFBTyxFQUFoQztHQUhEOzs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7OztFQWdDQyxJQUFBLEdBQU8sR0FBRyxDQUFDLEdBQUosQ0FBUSxDQUFBLEdBQUUsR0FBVixFQUFjLENBQUEsR0FBRSxHQUFoQixFQUFvQixDQUFwQixFQUFzQixDQUF0QjtTQUNQLElBQUksQ0FBQyxVQUFMLENBQUE7QUFsQ1ksRUEvRGI7OztBQW9HQSxJQUFBLEdBQU8sUUFBQSxDQUFBLENBQUE7QUFDUCxNQUFBLENBQUEsRUFBQSxLQUFBLEVBQUEsQ0FBQSxFQUFBLENBQUEsRUFBQSxHQUFBLEVBQUEsR0FBQSxFQUFBLE9BQUEsRUFBQSxLQUFBLEVBQUEsRUFBQSxFQUFBLEVBQUEsRUFBQSxFQUFBLEVBQUE7RUFBQyxVQUFBLENBQVcsTUFBWDtFQUNBLEtBQUEsQ0FBTSxHQUFOLEVBQVUsQ0FBVixFQUFZLENBQVo7RUFDQSxJQUFBLENBQUssS0FBTDtFQUNBLE1BQUEsQ0FBTyxLQUFQO0VBRUEsS0FBQSxHQUFRO0VBQ1IsSUFBQSxDQUFLLEtBQUw7RUFFQSxFQUFBLEdBQUssS0FBQSxDQUFNLElBQUEsQ0FBSyxDQUFMLEVBQU8sRUFBQSxHQUFHLENBQVYsRUFBWSxHQUFBLEdBQUksRUFBaEIsQ0FBTjtFQUNMLEVBQUEsR0FBSyxLQUFBLENBQU0sSUFBQSxDQUFLLENBQUwsRUFBTyxFQUFBLEdBQUcsQ0FBVixFQUFZLEdBQUEsR0FBSSxFQUFoQixDQUFOO0VBQ0wsRUFBQSxHQUFLLEtBQUEsQ0FBTSxJQUFBLENBQUssQ0FBTCxFQUFPLEVBQUEsR0FBRyxDQUFWLEVBQVksQ0FBQyxHQUFBLEdBQUksQ0FBTCxDQUFBLEdBQVEsRUFBcEIsQ0FBTjtFQUNMLEVBQUEsR0FBSyxLQUFBLENBQU0sSUFBQSxDQUFLLENBQUwsRUFBTyxFQUFBLEdBQUcsQ0FBVixFQUFZLENBQUMsR0FBQSxHQUFJLENBQUwsQ0FBQSxHQUFRLEVBQXBCLENBQU47RUFFTCxJQUFBLENBQUssRUFBTCxFQUFRLEVBQVIsRUFBVyxFQUFYLEVBQWMsRUFBZDtFQUNBLElBQUEsQ0FBSyxFQUFMLEVBQVEsRUFBUixFQUFXLEVBQVgsRUFBYyxFQUFkO0VBQ0EsSUFBQSxDQUFLLEVBQUwsRUFBUSxFQUFSLEVBQVcsRUFBWCxFQUFjLEVBQWQ7RUFDQSxJQUFBLENBQUssRUFBTCxFQUFRLEVBQVIsRUFBVyxFQUFYLEVBQWMsRUFBZDtFQUVBLElBQUEsQ0FBSyxHQUFMO0VBQ0EsSUFBQSxDQUFLLEdBQUwsRUFBUyxHQUFULEVBQWEsR0FBYixFQUFpQixHQUFqQjtFQUVBLFFBQUEsQ0FBQTtFQUNBLElBQUcsSUFBSSxDQUFDLE1BQVI7QUFDQztBQUFBO0lBQUEsS0FBQSxxQ0FBQTs7OztBQUNDO0FBQUE7UUFBQSxLQUFBLHdDQUFBOztVQUNDLEtBQUEsR0FBUSxDQUFBLEdBQUksQ0FBSixHQUFRO1VBQ2hCLElBQUEsQ0FBSyxJQUFJLENBQUMsTUFBTSxDQUFDLENBQUEsR0FBRSxLQUFILENBQWhCO3dCQUNBLE1BQUEsQ0FBTyxHQUFBLEdBQUksQ0FBQSxHQUFFLEVBQWIsRUFBZ0IsR0FBQSxHQUFJLENBQUEsR0FBRSxFQUF0QixFQUF5QixFQUF6QjtRQUhELENBQUE7OztJQURELENBQUE7bUJBREQ7O0FBdkJNIiwic291cmNlc0NvbnRlbnQiOlsiZWNobyA9IGNvbnNvbGUubG9nXHJcbnJhbmdlID0gXy5yYW5nZVxyXG5cclxuaW1nID0gbnVsbFxyXG5ydXRhID0gbnVsbFxyXG5cclxucm93ID0gMFxyXG5jb2wgPSAwXHJcblxyXG5OID0gMzBcclxuXHJcbnByZWxvYWQgPSAtPlxyXG5cdGltZyA9IGxvYWRJbWFnZSBcIlRlMmU0LmpwZ1wiXHJcblx0XHJcbnNldHVwID0gLT5cclxuXHRjcmVhdGVDYW52YXMgaW1nLndpZHRoLGltZy5oZWlnaHRcclxuXHRub0ZpbGwoKVxyXG5cdHRleHRTaXplIDM2XHJcblx0ZmlsbCAwXHJcblxyXG5cdHJ1dGEgPSBpbWcuZ2V0IE4qY29sLE4qcm93LE4sTlxyXG5cdHJ1dGEubG9hZFBpeGVscygpXHJcblxyXG4jIGZhY2l0ID0gXCJcIlwiZDJkNCBnN2c2XHJcbiMgYzFmNCBmOGc3XHJcbiMgZTJlMyBnOGY2XHJcbiMgYjFkMiBlODc4XHJcbiMgZzFmMyBkN2Q2XHJcbiMgZjFkMyBiN2I2XHJcbiMgaDJoMyBjOGI3XHJcbiMgZzJnNCBmNmQ1XHJcbiMgZjRnMyBkNWI0XHJcbiMgZDNlMiBiOGQ3XHJcbiMgYzJjMyBiNGM2XHJcbiMgaDNoNCBkN2Y2XHJcbiMgZzRnNSBmNmQ3XHJcbiMgaDRoNSBlN2U2XHJcbiMgaDVnNiBmN2c2XHJcbiMgZTNlNCBkNmQ1XHJcbiMgYjJiNCBkNWU0XHJcbiMgZDJlNCBjNmQ0XHJcbiMgZjNkNCBiN2U0XHJcbiMgZDRlNiBnN2MzXHJcbiMgZTFmMSBkOGU3XHJcbiMgZTZmOCAxOGY4XHJcbiMgYTFjMSBlNGgxXHJcbiMgZDFiMyBnOGg4XHJcbiMgYjNjMyBlOGc4XHJcbiMgYzNjNyBoMWU0XHJcbiMgZTJnNCBlNGY1XHJcbiMgZzRlMiBmNTgzXHJcbiMgZjFlMSBmOGY1XHJcbiMgYzFkMSBmNWc1XHJcbiMgYzdkOCBnN2Y4XHJcbiMgZDhnNSBmOGI0XHJcbiMgZDFkMiBiNGIxXHJcbiMgZTJkMSBiMWU0XHJcbiMgZDJlMiBlNGgxXHJcbiMgZTFkMiBoMWM2XHJcbiMgZTJlOCBoOGc3XHJcbiMgZzVlNyBnN2g2XHJcbiMgZzNmNFwiXCJcIlxyXG5cclxua2V5UHJlc3NlZCA9ICgpIC0+XHJcblx0aWYga2V5ID09ICdBcnJvd1JpZ2h0JyB0aGVuIGNvbCArPSAxXHJcblx0aWYga2V5ID09ICdBcnJvd0xlZnQnIHRoZW4gY29sIC09IDFcclxuXHRpZiBrZXkgPT0gJ0Fycm93RG93bicgdGhlbiByb3cgKz0gMVxyXG5cdGlmIGtleSA9PSAnQXJyb3dVcCcgdGhlbiByb3cgLT0gMVxyXG5cdCMgaWYga2V5ID09ICcgJ1xyXG5cdCMgXHRsaW5lcyA9IFtdXHJcblx0IyBcdGZvciBkcmFnIGluIHJhbmdlIDM5XHJcblx0IyBcdCAgICBmb3IgaXggaW4gWzEsNiwxMiwxN11cclxuXHQjIFx0ICAgICAgICBsZXR0ZXIgPSBmYWNpdFtkcmFnXVtpeF1cclxuICAgICMgICAgICAgICAgICAgaWYgbGV0dGVyIG5vdCBpbiBcImFiY2RlZmdoXCIgdGhlbiBjb250aW51ZVxyXG4gICAgIyAgICAgICAgICAgICByb3cgPSBkcmFnICUgMjBcclxuICAgICMgICAgICAgICAgICAgY29sb2Zmc2V0ID0gMiAqIChkcmFnIC8vIDIwKVxyXG4gICAgIyAgICAgICAgICAgICBjb2wgPSBpeCAlIDIgKyBjb2xvZmZzZXRcclxuICAgICMgICAgICAgICAgICAgaW5kZXggPSByb3cgKiAzMyArIFsxLDYsMTIsMTddW2NvbF1cclxuXHJcbiAgICAjICAgICAgICAgICAgIGZhY2l0UnV0YSA9IGxldHRlclxyXG5cclxuICAgICMgICAgICAgICBpZiBmYWNpdFJ1dGEgaW4gXCJhYmNkZWZnaFwiXHJcbiAgICAjICAgICAgICAgICAgIHJ1dGEgPSBpbWcuZ2V0IE4qY29sLE4qcm93LE4sTlxyXG4gICAgIyAgICAgICAgICAgICBydXRhLmxvYWRQaXhlbHMoKVxyXG4gICAgIyAgICAgICAgICAgICByYWQgPSBbe2E6XCIzNlwiLCBiOlwiMzdcIixjOiczOCcsIGQ6XCIzOVwiLGU6XCI0MFwiLCBmOlwiNDFcIixnOic0MicsIGg6XCI0M1wifVtmYWNpdFJ1dGFdXVxyXG4gICAgIyAgICAgICAgICAgICBmb3IgaSBpbiByYW5nZSAxLDI5XHJcbiAgICAjICAgICAgICAgICAgICAgICBmb3IgaiBpbiByYW5nZSAxLDI5XHJcbiAgICAjICAgICAgICAgICAgICAgICAgICAgaW5kZXggPSBOICogaiArIGlcclxuICAgICMgICAgICAgICAgICAgICAgICAgICByYWQucHVzaCBzdHIgMjU1IC0gcnV0YS5waXhlbHNbNCppbmRleF1cclxuICAgICMgICAgICAgICAgICAgcHJpbnQgcmFkLmxlbmd0aFxyXG4gICAgIyAgICAgICAgICAgICBsaW5lcy5wdXNoIHJhZC5qb2luKFwiLFwiKVxyXG5cdCMgXHRzYXZlU3RyaW5ncyBsaW5lcywnVGUyZTQnLCdjc3YnXHJcblx0IyBcdHJvdyA9IDBcclxuXHQjIFx0Y29sID0gMFxyXG5cdCMgZWxzZVxyXG5cdCMgZmV0Y2ggMjh4MjggbWF0cml4XHJcblx0cnV0YSA9IGltZy5nZXQgTipjb2wsTipyb3csTixOXHJcblx0cnV0YS5sb2FkUGl4ZWxzKClcclxuXHRcdCMgZWNobyBydXRhLnBpeGVsc1xyXG5cclxuZHJhdyA9IC0+XHJcblx0YmFja2dyb3VuZCBcImdyYXlcIlxyXG5cdGltYWdlIGltZywwLDBcclxuXHRmaWxsICdyZWQnXHJcblx0c3Ryb2tlICdyZWQnXHJcblxyXG5cdHNtYWxsID0gW11cclxuXHRmaWxsICdyZWQnXHJcblxyXG5cdHhhID0gcm91bmQgbGVycCAwLDMzKk4sY29sLzMzXHJcblx0eWEgPSByb3VuZCBsZXJwIDAsMjAqTixyb3cvMjBcclxuXHR4YiA9IHJvdW5kIGxlcnAgMCwzMypOLChjb2wrMSkvMzNcclxuXHR5YiA9IHJvdW5kIGxlcnAgMCwyMCpOLChyb3crMSkvMjBcclxuXHJcblx0bGluZSB4YSx5YSx4Yix5YVxyXG5cdGxpbmUgeGIseWEseGIseWJcclxuXHRsaW5lIHhhLHliLHhiLHliXHJcblx0bGluZSB4YSx5YSx4YSx5YlxyXG5cclxuXHRmaWxsIDI1NVxyXG5cdHJlY3QgNjIwLDI4MCwyODAsMjgwXHJcblxyXG5cdG5vU3Ryb2tlKClcclxuXHRpZiBydXRhLnBpeGVsc1xyXG5cdFx0Zm9yIGkgaW4gcmFuZ2UgMjhcclxuXHRcdFx0Zm9yIGogaW4gcmFuZ2UgMjhcclxuXHRcdFx0XHRpbmRleCA9IE4gKiBqICsgaVxyXG5cdFx0XHRcdGZpbGwgcnV0YS5waXhlbHNbNCppbmRleF1cclxuXHRcdFx0XHRjaXJjbGUgNjIwK2kqMTAsMjgwK2oqMTAsMTBcclxuIl19
//# sourceURL=c:\github\2024\013-create_abcdefgh\coffee\showjpg.coffee