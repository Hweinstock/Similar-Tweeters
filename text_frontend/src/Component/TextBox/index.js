import React, { Component } from "react";

export default class TextBox extends Component {

  render() {
    return (
        <div>
          <label>Text{this.props.name}: </label>
          <textarea
                  onChange={(e) => this.props.handleChange(e, this.props.name)}
                    rows={5}
                    cols={5}
         />
        </div>
    );
  }
}