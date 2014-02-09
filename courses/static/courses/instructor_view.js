var N_STUDENTS = 100

var t = 1297110663, // start time (seconds since epoch)
    v = 70, // start value (subscribers)
    data = d3.range(33).map(next); // starting dataset

function next() {
  return {
    time: ++t,
    value: v = ~~Math.max(10, Math.min(90, v + 10 * (Math.random() - .5)))
  };
}

setInterval(function() {
  data.shift();
  data.push(next());
  redraw();
}, 1500);

var w = 20,
    h = 200;

var x = d3.scale.linear()
    .domain([0, 1])
    .range([0, w]);

var y = d3.scale.linear()
    .domain([0, N_STUDENTS])
    .rangeRound([0, h]);

var yAxis = d3.svg.axis()
    .scale(d3.scale.linear().domain([0, N_STUDENTS]).rangeRound([h, 0]))
    .tickValues([N_STUDENTS / 10, N_STUDENTS - N_STUDENTS / 10])
    .tickSize(-w/10, w/10)
    .orient("left");

var chart = d3.select("body").append("svg")
    .attr("class", "chart")
    .attr("width", w * data.length - 1)
    .attr("height", h);

chart.append("line")
    .attr("x1", 0)
    .attr("x2", w * data.length)
    .attr("y1", h - .5)
    .attr("y2", h - .5)
    .style("stroke", "#000");

chart.append("g")
    .attr("class", "axis")
    .call(yAxis)
    .attr("transform", "translate(30,0)");
    //.attr("stroke", "black");
    //.attr("stroke-width", 2);


redraw();

function redraw() {

  var rect = chart.selectAll("rect")
      .data(data, function(d) { return d.time; });

  rect.enter().insert("rect", "line")
      .attr("x", function(d, i) { return x(i + 1) - .5; })
      .attr("y", function(d) { return h - y(d.value) - .5; })
      .attr("width", w)
      .attr("fill", "#3399FF")
      .attr("height", function(d) { return y(d.value); })
    .transition()
      .duration(1000)
      .attr("x", function(d, i) { return x(i) - .5; });

  rect.transition()
      .duration(1000)
      .attr("x", function(d, i) { return x(i) - .5; });

  rect.exit().transition()
      .duration(1000)
      .attr("x", function(d, i) { return x(i - 1) - .5; })
      .remove();
}
