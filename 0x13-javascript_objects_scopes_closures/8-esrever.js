#!/usr/bin/node

exports.esrever = function (list) {
  let lenght = list.length - 1;
  let a = 0;
  while ((lenght - a) > 0) {
    const varr = list[lenght];
    list[lenght] = list[a];
    list[a] = varr;
    a++;
    lenght--;
  }

  return list;
};
