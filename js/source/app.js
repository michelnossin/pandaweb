'use strict';

import React from 'react';
import ReactDOM from 'react-dom';
import PandaWeb from './components/PandaWeb';

ReactDOM.render(
  <div>
  <h1>Panda Dataframe. Show it all:</h1>
  <PandaWeb />
  <h1>Show range:</h1>
  <PandaWeb url="http://localhost:3000/pandaweb/range/5/10"/>
  </div>,
  document.getElementById('app')
);
