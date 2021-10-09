import React, { Component } from "react";
import textBoxStyling from "./styling/textBox.module.css"
export default class TextBox extends Component {


  render() {
    return (
        <div className={textBoxStyling.textBoxBorder}>
          <textarea
                  onChange={(e) => this.props.handleChange(e, this.props.name)}
                    rows={30}
                    cols={50}
                    placeholder="Enter text here. "
         />
        </div>
    );
  }
}