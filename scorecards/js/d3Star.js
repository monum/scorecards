function d3Star () {

    var size = 20,
        x = 0,
        y = 0,
        value = 1.0, //Range is 0.0 - 1.0
        borderWidth = 3,
        borderColor = "black",
        starColor = "#FFB500",
        backgroundColor = "white";

    function star (selection) {

        var line = d3.svg.line().x(function(d){ return d.x; }).y(function(d){ return d.y; })
                .interpolate("linear-closed"),
            rad = function (deg) { return deg * Math.PI/180;},
            cos = function (deg) { return Math.cos(rad(deg)); },
            sin = function (deg) { return Math.sin(rad(deg)); },
            tan  = function (deg) { return Math.tan(rad(deg));},
            n = size,
            m = n / 2,
            h = m * tan(36),
            k = h / sin(72),

            //(x, y) points at the leftmost point of the star, not the center
            coordinates = [
                {x: x, y: y},
                {x: x + k, y: y},
                {x: x + m, y: y - h},
                {x: x + n - k, y: y},
                {x: x + n, y: y},
                {x: x + n - k * cos(36), y: y + k * sin(36)},
                {x: x + n * cos(36), y: y + n * sin(36)},
                {x: x + m, y: y + h},
                {x: x + n - n * cos(36),y: y + n * sin(36)},
                {x: x + k * cos(36), y: y + k * sin(36)},
            ];

        //inside star
        selection.append("path").attr("d", line(coordinates)).style({ "stroke-width": 0, "fill": starColor});

        //Rect for clipping
        //In order to avoid potential ID duplicates for clipping, clip-path is not used here
        selection.append("rect").attr("x", x + (size * value)).attr("y", y - h)
            .attr("width", size - size * value).attr("height", size).style("fill", backgroundColor);

        //border of the star
        selection.append("path").attr("d", line(coordinates))
            .style({ "stroke-width": borderWidth, "fill": "none", "stroke": borderColor});


    }

    star.x = function (val) {
        x = val;
        return star;
    }

    star.y = function (val) {
        y = val;
        return star;
    }

    star.size = function (val) {
        size = val;
        return star;
    }

    //Range is 0.0 - 1.0. 0.0 shows, for example, an empty star
    star.value = function (val) {
        value = val;
        return star;
    }

    star.backgroundColor = function (val) {
        backgroundColor = val;
        return star;
    }

    star.borderWidth = function (val) {
        borderWidth = val;
        return star;
    }

    star.borderColor = function (val) {
        borderColor = val;
        return star;
    }

    star.starColor = function (val) {
        starColor = val;
        return star;
    }

    star.isBorderRounded = function (val) {
        isBorderRounded = val;
        return star;
    }

    return star;
}
