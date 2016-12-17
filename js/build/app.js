'use strict';

var _react = require('react');

var _react2 = _interopRequireDefault(_react);

var _reactDom = require('react-dom');

var _reactDom2 = _interopRequireDefault(_reactDom);

var _PandaWeb = require('./components/PandaWeb');

var _PandaWeb2 = _interopRequireDefault(_PandaWeb);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

_reactDom2.default.render(_react2.default.createElement(
  'div',
  null,
  _react2.default.createElement(
    'h1',
    null,
    'Panda Dataframe. Show it all:'
  ),
  _react2.default.createElement(_PandaWeb2.default, null),
  _react2.default.createElement(
    'h1',
    null,
    'Show range:'
  ),
  _react2.default.createElement(_PandaWeb2.default, { url: 'http://localhost:3000/pandaweb/range/5/10' })
), document.getElementById('app'));