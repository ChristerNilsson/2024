// Generated by CoffeeScript 2.7.0
var ActiveComputerHouse, Button, Evaluate, FinalScoring, HasSuccessors, HouseButtonActive, HouseOnClick, Relocation, beans, buttons, depth, keyPressed, messages, mousePressed, myscale, player, playerComputer, playerTitle, reset, setup, xdraw;

playerTitle = ['Human', 'Computer'];

playerComputer = [false, true];

player = 0; // 0 or 1

beans = 4;

depth = 1;

buttons = [];

myscale = 1;

messages = {};

messages.depth = depth;

messages.time = 0;

messages.result = '';

messages.computerLetters = '';

messages.humanLetters = '';

messages.moves = 0;

Button = class Button {
  constructor(x1, y1, value, littera1 = '', click = function() {}) {
    this.x = x1;
    this.y = y1;
    this.value = value;
    this.littera = littera1;
    this.click = click;
    this.radie = myscale * 40;
  }

  draw() {
    fc(1, 0, 0);
    circle(this.x, this.y, this.radie);
    textAlign(CENTER, CENTER);
    if (this.value > 0) {
      fc(1);
      return text(this.value, this.x, this.y);
    } else {
      push();
      fc(0.8, 0, 0);
      text(this.littera, this.x, this.y);
      return pop();
    }
  }

  inside(x, y) {
    return this.radie > dist(x, y, this.x, this.y);
  }

};

setup = function() {
  var i, j, k, len, len1, littera, params, ref, ref1;
  params = getURLParams();
  if (params.scale) {
    myscale = params.scale;
  }
  createCanvas(myscale * 2 * 450, myscale * 2 * 150);
  textAlign(CENTER, CENTER);
  textSize(myscale * 40);
  ref = 'abcdef';
  for (i = j = 0, len = ref.length; j < len; i = ++j) {
    littera = ref[i];
    (function(i) {
      return buttons.push(new Button(myscale * 2 * 100 + myscale * 2 * 50 * i, myscale * 2 * 100, beans, '', function() {
        return HouseOnClick(i);
      }));
    })(i);
  }
  buttons.push(new Button(myscale * 2 * 400, myscale * 2 * 75, 0));
  ref1 = 'ABCDEF';
  for (i = k = 0, len1 = ref1.length; k < len1; i = ++k) {
    littera = ref1[i];
    buttons.push(new Button(myscale * 2 * 100 + myscale * 2 * 50 * (5 - i), myscale * 2 * 50, beans, littera));
  }
  buttons.push(new Button(myscale * 2 * 50, myscale * 2 * 75, 0));
  return reset(beans);
};

xdraw = function() {
  var button, j, len;
  bg(0);
  for (j = 0, len = buttons.length; j < len; j++) {
    button = buttons[j];
    button.draw();
  }
  fc(1, 1, 0);
  textAlign(LEFT, CENTER);
  text('Level: ' + messages.depth, myscale * 2 * 10, myscale * 2 * 20);
  text(messages.result, myscale * 2 + 10, myscale * 2 * 135);
  textAlign(CENTER, CENTER);
  text(messages.computerLetters, width / 2, myscale * 2 * 20);
  text(messages.humanLetters, width / 2, myscale * 2 * 135);
  textAlign(RIGHT, CENTER);
  text(Math.round(10 * messages.time) / 10 + ' ms', width - 2 * 10, myscale * 2 * 20);
  return text(messages.moves, width - 2 * 10, myscale * 2 * 135);
};

mousePressed = function() {
  var button, j, len, results;
  if (messages.result !== '') {
    return reset(0);
  }
  messages.computerLetters = '';
  console.log(mouseX, mouseY);
  results = [];
  for (j = 0, len = buttons.length; j < len; j++) {
    button = buttons[j];
    if (button.inside(mouseX, mouseY)) {
      results.push(button.click());
    } else {
      results.push(void 0);
    }
  }
  return results;
};

reset = function(b) {
  var button, j, len;
  if (b > 0) {
    beans = b;
  }
  for (j = 0, len = buttons.length; j < len; j++) {
    button = buttons[j];
    button.value = beans;
  }
  buttons[6].value = 0;
  buttons[13].value = 0;
  if (depth < 1) {
    depth = 1;
  }
  messages.depth = depth;
  messages.time = 0;
  messages.result = '';
  messages.computerLetters = '';
  messages.moves = 0;
  player = _.random(0, 1);
  if (player === 1) {
    ActiveComputerHouse();
  }
  console.log(player);
  return xdraw();
};

keyPressed = function() {
  var index;
  if (messages.result === '') {
    return;
  }
  index = " 1234567890".indexOf(key);
  if (index >= 0) {
    return reset(index);
  }
};

ActiveComputerHouse = function() {
  var result, start, stopp;
  start = window.performance.now();
  result = alphaBeta(depth, player);
  stopp = window.performance.now();
  messages.time += stopp - start;
  return HouseOnClick(result);
};

HouseButtonActive = function() {
  if (playerComputer[player]) {
    return ActiveComputerHouse();
  }
};

HouseOnClick = function(pickedHouse) {
  var again, house, i, j, k, len, len1, ref, ref1;
  if (pickedHouse >= 7) {
    messages.computerLetters += 'abcdef ABCDEF'[pickedHouse];
  } else {
    messages.humanLetters += 'abcdef ABCDEF'[pickedHouse];
  }
  xdraw();
  if (buttons[pickedHouse].value === 0) {
    return;
  }
  house = buttons.map(function(button) {
    return button.value;
  });
  again = Relocation(house, pickedHouse);
  ref = range(14);
  for (j = 0, len = ref.length; j < len; j++) {
    i = ref[j];
    buttons[i].value = house[i];
  }
  if (again) {

  } else {
    if (player === 1) {
      console.log(messages.computerLetters);
      console.log(messages.humanLetters);
      messages.moves++;
    }
    player = 1 - player;
  }
  if (HasSuccessors(house)) {
    if (player === 1) {
      messages.humanLetters = '';
    }
    HouseButtonActive();
  } else {
    FinalScoring(house);
    ref1 = range(14);
    for (k = 0, len1 = ref1.length; k < len1; k++) {
      i = ref1[k];
      buttons[i].value = house[i];
    }
    if (house[13] > house[6]) {
      messages.result = playerTitle[1] + " Wins";
      depth--;
    } else if (house[13] === house[6]) {
      messages.result = "Tie";
    } else {
      messages.result = playerTitle[0] + " Wins";
      depth++;
    }
    console.log('');
  }
  return xdraw();
};

Relocation = function(house, pickedHouse) {
  var index, opponentShop, playerShop, seeds;
  playerShop = 6;
  opponentShop = 13;
  if (pickedHouse > 6) {
    playerShop = 13;
    opponentShop = 6;
  }
  index = pickedHouse;
  seeds = house[pickedHouse];
  house[index] = 0;
  while (seeds > 0) {
    index = (index + 1) % 14;
    if (index === opponentShop) {
      continue;
    }
    house[index]++;
    seeds--;
  }
  if (index === playerShop) {
    return true;
  }
  if (house[index] === 1 && house[12 - index] !== 0 && index >= (playerShop - 6) && index < playerShop) {
    house[playerShop] += house[12 - index] + 1;
    house[index] = house[12 - index] = 0;
  }
  return false;
};

FinalScoring = function(house) {
  var i, j, len, ref, results;
  ref = range(6);
  results = [];
  for (j = 0, len = ref.length; j < len; j++) {
    i = ref[j];
    house[6] += house[i];
    house[13] += house[7 + i];
    results.push(house[i] = house[7 + i] = 0);
  }
  return results;
};

Evaluate = function(house, player1, player2) {
  return house[player1] - house[player2];
};

HasSuccessors = function(house) {
  var i, j, len, player1, player2, ref;
  player1 = false;
  player2 = false;
  ref = range(6);
  for (j = 0, len = ref.length; j < len; j++) {
    i = ref[j];
    if (house[i] !== 0) {
      player1 = true;
    }
    if (house[7 + i] !== 0) {
      player2 = true;
    }
  }
  return player1 && player2;
};

//# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiaW5kZXguanMiLCJzb3VyY2VSb290IjoiLi5cXCIsInNvdXJjZXMiOlsiY29mZmVlXFxpbmRleC5jb2ZmZWUiXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IjtBQUFBLElBQUEsbUJBQUEsRUFBQSxNQUFBLEVBQUEsUUFBQSxFQUFBLFlBQUEsRUFBQSxhQUFBLEVBQUEsaUJBQUEsRUFBQSxZQUFBLEVBQUEsVUFBQSxFQUFBLEtBQUEsRUFBQSxPQUFBLEVBQUEsS0FBQSxFQUFBLFVBQUEsRUFBQSxRQUFBLEVBQUEsWUFBQSxFQUFBLE9BQUEsRUFBQSxNQUFBLEVBQUEsY0FBQSxFQUFBLFdBQUEsRUFBQSxLQUFBLEVBQUEsS0FBQSxFQUFBOztBQUFBLFdBQUEsR0FBYyxDQUFDLE9BQUQsRUFBUyxVQUFUOztBQUNkLGNBQUEsR0FBaUIsQ0FBQyxLQUFELEVBQU8sSUFBUDs7QUFDakIsTUFBQSxHQUFTLEVBRlQ7O0FBR0EsS0FBQSxHQUFROztBQUNSLEtBQUEsR0FBUTs7QUFDUixPQUFBLEdBQVc7O0FBQ1gsT0FBQSxHQUFVOztBQUVWLFFBQUEsR0FBVyxDQUFBOztBQUNYLFFBQVEsQ0FBQyxLQUFULEdBQWlCOztBQUNqQixRQUFRLENBQUMsSUFBVCxHQUFnQjs7QUFDaEIsUUFBUSxDQUFDLE1BQVQsR0FBa0I7O0FBQ2xCLFFBQVEsQ0FBQyxlQUFULEdBQTJCOztBQUMzQixRQUFRLENBQUMsWUFBVCxHQUF3Qjs7QUFDeEIsUUFBUSxDQUFDLEtBQVQsR0FBaUI7O0FBRVgsU0FBTixNQUFBLE9BQUE7RUFDQyxXQUFjLEdBQUEsSUFBQSxPQUFBLGFBQXVCLEVBQXZCLFVBQWlDLFFBQUEsQ0FBQSxDQUFBLEVBQUEsQ0FBakMsQ0FBQTtJQUFDLElBQUMsQ0FBQTtJQUFFLElBQUMsQ0FBQTtJQUFFLElBQUMsQ0FBQTtJQUFNLElBQUMsQ0FBQTtJQUFXLElBQUMsQ0FBQTtJQUFhLElBQUMsQ0FBQSxLQUFELEdBQU8sT0FBQSxHQUFRO0VBQXZEOztFQUNkLElBQU8sQ0FBQSxDQUFB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LENBQUMsQ0FBQSxHQUFJLENBQUw7aUJBQ2xCLEtBQUssQ0FBQyxDQUFELENBQUwsR0FBVyxLQUFLLENBQUMsQ0FBQSxHQUFJLENBQUwsQ0FBTCxHQUFlO0VBSDNCLENBQUE7O0FBRGM7O0FBTWYsUUFBQSxHQUFXLFFBQUEsQ0FBQyxLQUFELEVBQVEsT0FBUixFQUFpQixPQUFqQixDQUFBO1NBQTZCLEtBQUssQ0FBQyxPQUFELENBQUwsR0FBaUIsS0FBSyxDQUFDLE9BQUQ7QUFBbkQ7O0FBRVgsYUFBQSxHQUFnQixRQUFBLENBQUMsS0FBRCxDQUFBO0FBQ2hCLE1BQUEsQ0FBQSxFQUFBLENBQUEsRUFBQSxHQUFBLEVBQUEsT0FBQSxFQUFBLE9BQUEsRUFBQTtFQUFDLE9BQUEsR0FBVTtFQUNWLE9BQUEsR0FBVTtBQUNWO0VBQUEsS0FBQSxxQ0FBQTs7SUFDQyxJQUFHLEtBQUssQ0FBQyxDQUFELENBQUwsS0FBWSxDQUFmO01BQXNCLE9BQUEsR0FBVSxLQUFoQzs7SUFDQSxJQUFHLEtBQUssQ0FBQyxDQUFBLEdBQUksQ0FBTCxDQUFMLEtBQWdCLENBQW5CO01BQTBCLE9BQUEsR0FBVSxLQUFwQzs7RUFGRDtTQUdBLE9BQUEsSUFBWTtBQU5HIiwic291cmNlc0NvbnRlbnQiOlsicGxheWVyVGl0bGUgPSBbJ0h1bWFuJywnQ29tcHV0ZXInXVxyXG5wbGF5ZXJDb21wdXRlciA9IFtmYWxzZSx0cnVlXVxyXG5wbGF5ZXIgPSAwICMgMCBvciAxXHJcbmJlYW5zID0gNFxyXG5kZXB0aCA9IDFcclxuYnV0dG9ucyAgPSBbXVxyXG5teXNjYWxlID0gMVxyXG5cclxubWVzc2FnZXMgPSB7fVxyXG5tZXNzYWdlcy5kZXB0aCA9IGRlcHRoXHJcbm1lc3NhZ2VzLnRpbWUgPSAwXHJcbm1lc3NhZ2VzLnJlc3VsdCA9ICcnXHJcbm1lc3NhZ2VzLmNvbXB1dGVyTGV0dGVycyA9ICcnXHJcbm1lc3NhZ2VzLmh1bWFuTGV0dGVycyA9ICcnXHJcbm1lc3NhZ2VzLm1vdmVzID0gMFxyXG5cclxuY2xhc3MgQnV0dG9uXHJcblx0Y29uc3RydWN0b3IgOiAoQHgsQHksQHZhbHVlLEBsaXR0ZXJhPScnLEBjbGljaz0tPikgLT4gQHJhZGllPW15c2NhbGUqNDBcclxuXHRkcmF3IDogLT5cclxuXHRcdGZjIDEsMCwwXHJcblx0XHRjaXJjbGUgQHgsQHksQHJhZGllXHJcblx0XHR0ZXh0QWxpZ24gQ0VOVEVSLENFTlRFUlxyXG5cdFx0aWYgQHZhbHVlID4gMCBcclxuXHRcdFx0ZmMgMVxyXG5cdFx0XHR0ZXh0IEB2YWx1ZSxAeCxAeVxyXG5cdFx0ZWxzZVxyXG5cdFx0XHRwdXNoKClcclxuXHRcdFx0ZmMgMC44LDAsMFxyXG5cdFx0XHR0ZXh0IEBsaXR0ZXJhLEB4LEB5XHJcblx0XHRcdHBvcCgpXHJcblx0aW5zaWRlIDogKHgseSkgLT4gQHJhZGllID4gZGlzdCB4LHksQHgsQHlcclxuXHJcbnNldHVwID0gLT5cclxuXHRwYXJhbXMgPSBnZXRVUkxQYXJhbXMoKVxyXG5cdGlmIHBhcmFtcy5zY2FsZSB0aGVuIG15c2NhbGUgPSBwYXJhbXMuc2NhbGVcclxuXHRjcmVhdGVDYW52YXMgbXlzY2FsZSoyKjQ1MCxteXNjYWxlKjIqMTUwXHJcblx0dGV4dEFsaWduIENFTlRFUixDRU5URVJcclxuXHR0ZXh0U2l6ZSBteXNjYWxlICogNDBcclxuXHRmb3IgbGl0dGVyYSxpIGluICdhYmNkZWYnXHJcblx0XHRkbyAoaSkgLT5cclxuXHRcdFx0YnV0dG9ucy5wdXNoIG5ldyBCdXR0b24gbXlzY2FsZSoyKjEwMCArIG15c2NhbGUqMio1MCppLCBteXNjYWxlKjIqMTAwLGJlYW5zLCcnLCgpIC0+IEhvdXNlT25DbGljayBpXHJcblx0YnV0dG9ucy5wdXNoIG5ldyBCdXR0b24gbXlzY2FsZSoyKjQwMCwgbXlzY2FsZSoyKjc1LDBcclxuXHRmb3IgbGl0dGVyYSxpIGluICdBQkNERUYnXHJcblx0XHRidXR0b25zLnB1c2ggbmV3IEJ1dHRvbiBteXNjYWxlKjIqMTAwICsgbXlzY2FsZSoyKjUwKig1LWkpLCBteXNjYWxlKjIqNTAsIGJlYW5zLCBsaXR0ZXJhXHJcblx0YnV0dG9ucy5wdXNoIG5ldyBCdXR0b24gbXlzY2FsZSoyKjUwLCBteXNjYWxlKjIqNzUsMFxyXG5cdHJlc2V0IGJlYW5zXHJcblxyXG54ZHJhdyA9IC0+XHJcblx0YmcgMFxyXG5cdGZvciBidXR0b24gaW4gYnV0dG9uc1xyXG5cdFx0YnV0dG9uLmRyYXcoKVxyXG5cdGZjIDEsMSwwXHJcblx0dGV4dEFsaWduIExFRlQsQ0VOVEVSXHJcblx0dGV4dCAnTGV2ZWw6ICcrbWVzc2FnZXMuZGVwdGgsbXlzY2FsZSAqIDIqMTAsIG15c2NhbGUgKiAyKjIwXHJcblx0dGV4dCBtZXNzYWdlcy5yZXN1bHQsbXlzY2FsZSAqIDIrMTAsIG15c2NhbGUgKiAyKjEzNVxyXG5cdHRleHRBbGlnbiBDRU5URVIsQ0VOVEVSXHJcblx0dGV4dCBtZXNzYWdlcy5jb21wdXRlckxldHRlcnMsd2lkdGgvMixteXNjYWxlICogMioyMFxyXG5cdHRleHQgbWVzc2FnZXMuaHVtYW5MZXR0ZXJzLHdpZHRoLzIsbXlzY2FsZSAqIDIqMTM1XHJcblx0dGV4dEFsaWduIFJJR0hULENFTlRFUlxyXG5cdHRleHQgTWF0aC5yb3VuZCgxMCptZXNzYWdlcy50aW1lKS8xMCArICcgbXMnLCAod2lkdGgtMioxMCksICBteXNjYWxlICogMioyMFxyXG5cdHRleHQgbWVzc2FnZXMubW92ZXMsICh3aWR0aC0yKjEwKSwgbXlzY2FsZSAqIDIqMTM1XHJcblxyXG5tb3VzZVByZXNzZWQgPSAoKSAtPlxyXG5cdGlmIG1lc3NhZ2VzLnJlc3VsdCAhPSAnJyB0aGVuIHJldHVybiByZXNldCAwXHJcblx0bWVzc2FnZXMuY29tcHV0ZXJMZXR0ZXJzID0gJydcclxuXHRjb25zb2xlLmxvZyBtb3VzZVgsbW91c2VZXHJcblx0Zm9yIGJ1dHRvbiBpbiBidXR0b25zXHJcblx0XHRpZiBidXR0b24uaW5zaWRlIG1vdXNlWCxtb3VzZVkgdGhlbiBidXR0b24uY2xpY2soKVxyXG5cclxucmVzZXQgPSAoYikgLT5cclxuXHRpZiBiID4gMCB0aGVuXHRiZWFucyA9IGJcclxuXHRmb3IgYnV0dG9uIGluIGJ1dHRvbnNcclxuXHRcdGJ1dHRvbi52YWx1ZSA9IGJlYW5zXHJcblx0YnV0dG9uc1s2XS52YWx1ZSA9IDBcclxuXHRidXR0b25zWzEzXS52YWx1ZSA9IDBcclxuXHRpZiBkZXB0aCA8IDEgdGhlbiBkZXB0aCA9IDFcclxuXHRtZXNzYWdlcy5kZXB0aCA9IGRlcHRoXHJcblx0bWVzc2FnZXMudGltZSA9IDBcclxuXHRtZXNzYWdlcy5yZXN1bHQgPSAnJ1xyXG5cdG1lc3NhZ2VzLmNvbXB1dGVyTGV0dGVycyA9ICcnXHJcblx0bWVzc2FnZXMubW92ZXMgPSAwXHJcblxyXG5cdHBsYXllciA9IF8ucmFuZG9tIDAsMVxyXG5cdGlmIHBsYXllciA9PSAxIHRoZW4gQWN0aXZlQ29tcHV0ZXJIb3VzZSgpXHJcblx0Y29uc29sZS5sb2cgcGxheWVyXHJcblx0eGRyYXcoKVxyXG5cclxua2V5UHJlc3NlZCA9IC0+XHJcblx0aWYgbWVzc2FnZXMucmVzdWx0ID09ICcnIHRoZW4gcmV0dXJuXHJcblx0aW5kZXggPSBcIiAxMjM0NTY3ODkwXCIuaW5kZXhPZiBrZXlcclxuXHRpZiBpbmRleCA+PSAwIHRoZW4gcmVzZXQgaW5kZXhcclxuXHJcbkFjdGl2ZUNvbXB1dGVySG91c2UgPSAoKSAtPlxyXG5cdHN0YXJ0ID0gd2luZG93LnBlcmZvcm1hbmNlLm5vdygpXHJcblx0cmVzdWx0ID0gYWxwaGFCZXRhIGRlcHRoLCBwbGF5ZXJcclxuXHRzdG9wcCA9IHdpbmRvdy5wZXJmb3JtYW5jZS5ub3coKVxyXG5cdG1lc3NhZ2VzLnRpbWUgKz0gc3RvcHAgLSBzdGFydFxyXG5cdEhvdXNlT25DbGljayByZXN1bHRcclxuXHJcbkhvdXNlQnV0dG9uQWN0aXZlID0gKCkgLT4gaWYgcGxheWVyQ29tcHV0ZXJbcGxheWVyXSB0aGVuIEFjdGl2ZUNvbXB1dGVySG91c2UoKSBcclxuXHJcbkhvdXNlT25DbGljayA9IChwaWNrZWRIb3VzZSkgLT5cclxuXHRpZiBwaWNrZWRIb3VzZSA+PSA3XHJcblx0XHRtZXNzYWdlcy5jb21wdXRlckxldHRlcnMgKz0gJ2FiY2RlZiBBQkNERUYnW3BpY2tlZEhvdXNlXVxyXG5cdGVsc2VcclxuXHRcdG1lc3NhZ2VzLmh1bWFuTGV0dGVycyArPSAnYWJjZGVmIEFCQ0RFRidbcGlja2VkSG91c2VdXHJcblx0eGRyYXcoKVxyXG5cdGlmIGJ1dHRvbnNbcGlja2VkSG91c2VdLnZhbHVlID09IDAgdGhlbiByZXR1cm4gXHJcblx0aG91c2UgPSBidXR0b25zLm1hcCAoYnV0dG9uKSAtPiBidXR0b24udmFsdWVcclxuXHRhZ2FpbiA9IFJlbG9jYXRpb24gaG91c2UsIHBpY2tlZEhvdXNlXHJcblx0Zm9yIGkgaW4gcmFuZ2UgMTRcclxuXHRcdGJ1dHRvbnNbaV0udmFsdWUgPSBob3VzZVtpXVxyXG5cdGlmIGFnYWluIFxyXG5cdGVsc2VcclxuXHRcdGlmIHBsYXllcj09MVxyXG5cdFx0XHRjb25zb2xlLmxvZyBtZXNzYWdlcy5jb21wdXRlckxldHRlcnNcclxuXHRcdFx0Y29uc29sZS5sb2cgbWVzc2FnZXMuaHVtYW5MZXR0ZXJzXHJcblx0XHRcdG1lc3NhZ2VzLm1vdmVzKytcclxuXHRcdHBsYXllciA9IDEgLSBwbGF5ZXJcclxuXHRpZiBIYXNTdWNjZXNzb3JzIGhvdXNlXHJcblx0XHRpZiBwbGF5ZXI9PTEgdGhlbiBtZXNzYWdlcy5odW1hbkxldHRlcnMgPSAnJ1xyXG5cdFx0SG91c2VCdXR0b25BY3RpdmUoKVxyXG5cdGVsc2UgXHJcblx0XHRGaW5hbFNjb3JpbmcgaG91c2VcclxuXHRcdGZvciBpIGluIHJhbmdlIDE0XHJcblx0XHRcdGJ1dHRvbnNbaV0udmFsdWUgPSBob3VzZVtpXVxyXG5cclxuXHRcdGlmIGhvdXNlWzEzXSA+IGhvdXNlWzZdXHJcblx0XHRcdG1lc3NhZ2VzLnJlc3VsdCA9IHBsYXllclRpdGxlWzFdICsgXCIgV2luc1wiXHJcblx0XHRcdGRlcHRoLS1cclxuXHRcdGVsc2UgaWYgaG91c2VbMTNdID09IGhvdXNlWzZdXHJcblx0XHRcdG1lc3NhZ2VzLnJlc3VsdCA9IFwiVGllXCJcclxuXHRcdGVsc2VcclxuXHRcdFx0bWVzc2FnZXMucmVzdWx0ID0gcGxheWVyVGl0bGVbMF0gKyBcIiBXaW5zXCJcclxuXHRcdFx0ZGVwdGgrK1xyXG5cdFx0Y29uc29sZS5sb2cgJydcclxuXHR4ZHJhdygpXHJcblxyXG5SZWxvY2F0aW9uID0gKGhvdXNlLCBwaWNrZWRIb3VzZSkgLT5cclxuXHRwbGF5ZXJTaG9wID0gNlxyXG5cdG9wcG9uZW50U2hvcCA9IDEzXHJcblx0aWYgcGlja2VkSG91c2UgPiA2XHJcblx0XHRwbGF5ZXJTaG9wID0gMTNcclxuXHRcdG9wcG9uZW50U2hvcCA9IDZcclxuXHJcblx0aW5kZXggPSBwaWNrZWRIb3VzZVxyXG5cdHNlZWRzID0gaG91c2VbcGlja2VkSG91c2VdXHJcblx0aG91c2VbaW5kZXhdID0gMCBcclxuXHR3aGlsZSBzZWVkcyA+IDAgXHJcblx0XHRpbmRleCA9IChpbmRleCArIDEpICUgMTRcclxuXHRcdGlmIGluZGV4ID09IG9wcG9uZW50U2hvcCB0aGVuIGNvbnRpbnVlXHJcblx0XHRob3VzZVtpbmRleF0rK1xyXG5cdFx0c2VlZHMtLVxyXG5cclxuXHRpZiBpbmRleCA9PSBwbGF5ZXJTaG9wIHRoZW4gcmV0dXJuIHRydWVcclxuXHJcblx0aWYgaG91c2VbaW5kZXhdID09IDEgYW5kIGhvdXNlWzEyIC0gaW5kZXhdICE9IDAgYW5kIGluZGV4ID49IChwbGF5ZXJTaG9wIC0gNikgYW5kIGluZGV4IDwgcGxheWVyU2hvcFxyXG5cdFx0aG91c2VbcGxheWVyU2hvcF0gKz0gaG91c2VbMTIgLSBpbmRleF0gKyAxXHJcblx0XHRob3VzZVtpbmRleF0gPSBob3VzZVsxMiAtIGluZGV4XSA9IDBcclxuXHRmYWxzZVxyXG5cclxuRmluYWxTY29yaW5nID0gKGhvdXNlKSAtPlxyXG5cdGZvciBpIGluIHJhbmdlIDZcclxuXHRcdGhvdXNlWzZdICs9IGhvdXNlW2ldXHJcblx0XHRob3VzZVsxM10gKz0gaG91c2VbNyArIGldXHJcblx0XHRob3VzZVtpXSA9IGhvdXNlWzcgKyBpXSA9IDBcclxuXHJcbkV2YWx1YXRlID0gKGhvdXNlLCBwbGF5ZXIxLCBwbGF5ZXIyKSAtPiBob3VzZVtwbGF5ZXIxXSAtIGhvdXNlW3BsYXllcjJdXHJcblxyXG5IYXNTdWNjZXNzb3JzID0gKGhvdXNlKSAtPlxyXG5cdHBsYXllcjEgPSBmYWxzZVxyXG5cdHBsYXllcjIgPSBmYWxzZVxyXG5cdGZvciBpIGluIHJhbmdlIDZcclxuXHRcdGlmIGhvdXNlW2ldICE9IDAgdGhlbiBwbGF5ZXIxID0gdHJ1ZVxyXG5cdFx0aWYgaG91c2VbNyArIGldICE9IDAgdGhlbiBwbGF5ZXIyID0gdHJ1ZVxyXG5cdHBsYXllcjEgYW5kIHBsYXllcjJcclxuIl19
//# sourceURL=c:\github\Lab\2019\118-Kalaha\coffee\index.coffee