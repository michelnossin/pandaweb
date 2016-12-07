import React from 'react';
import Fetch from 'react-fetch'
//var React = require('react');
import Griddle from 'griddle-react';
//var Griddle = require('griddle-react');


class PandaWeb extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
        message: "WAITING FOR API",
        datatable: []
    };

    this.setData.bind(this)
  }

  setData(msg,data) {
     if (this.state.message != msg) {
       this.setState({message: msg,datatable: data })
     }
   }


  render() {
     var obj = this

    fetch(this.props.url, {
    	method: 'get'
    }).then(function(response) {

      var contentType = response.headers.get("content-type");
        if(contentType && contentType.indexOf("application/json") !== -1) {
          response.json().then(function(json) {
            console.log("OK we got json");
            obj.setData(json.message,json.datatable)

          });
        } else {
          console.log("Oops, we haven't got JSON!");
          obj.setData("Backend show no json",[])
        }

    }).catch(function(err) {
      console.log("Error , no API BACKEND");
      console.log(err);
      obj.setData("Backend not running",[])

    });

    return (
      <div className="Pandaweb">{this.state.message}<Griddle results={this.state.datatable}/></div>
    );
  }
}

PandaWeb.propTypes = {
    url: React.PropTypes.string
};

PandaWeb.defaultProps = {
    url: "http://localhost:8080/data",
};

export default PandaWeb;
