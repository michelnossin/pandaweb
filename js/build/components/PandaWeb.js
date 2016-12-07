'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

var _react = require('react');

var _react2 = _interopRequireDefault(_react);

var _reactFetch = require('react-fetch');

var _reactFetch2 = _interopRequireDefault(_reactFetch);

var _griddleReact = require('griddle-react');

var _griddleReact2 = _interopRequireDefault(_griddleReact);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }
//var React = require('react');


//var Griddle = require('griddle-react');


var PandaWeb = function (_React$Component) {
  _inherits(PandaWeb, _React$Component);

  function PandaWeb(props) {
    _classCallCheck(this, PandaWeb);

    var _this = _possibleConstructorReturn(this, (PandaWeb.__proto__ || Object.getPrototypeOf(PandaWeb)).call(this, props));

    _this.state = {
      message: "WAITING FOR API",
      datatable: []
    };

    _this.setData.bind(_this);
    return _this;
  }

  _createClass(PandaWeb, [{
    key: 'setData',
    value: function setData(msg, data) {
      if (this.state.message != msg) {
        this.setState({ message: msg, datatable: data });
      }
    }
  }, {
    key: 'render',
    value: function render() {
      var obj = this;

      fetch(this.props.url, {
        method: 'get'
      }).then(function (response) {

        var contentType = response.headers.get("content-type");
        if (contentType && contentType.indexOf("application/json") !== -1) {
          response.json().then(function (json) {
            console.log("OK we got json");
            obj.setData(json.message, json.datatable);
          });
        } else {
          console.log("Oops, we haven't got JSON!");
          obj.setData("Backend show no json", []);
        }
      }).catch(function (err) {
        console.log("Error , no API BACKEND");
        console.log(err);
        obj.setData("Backend not running", []);
      });

      return _react2.default.createElement(
        'div',
        { className: 'Pandaweb' },
        this.state.message,
        _react2.default.createElement(_griddleReact2.default, { results: this.state.datatable })
      );
    }
  }]);

  return PandaWeb;
}(_react2.default.Component);

PandaWeb.propTypes = {
  url: _react2.default.PropTypes.string
};

PandaWeb.defaultProps = {
  url: "http://localhost:8080/data"
};

exports.default = PandaWeb;