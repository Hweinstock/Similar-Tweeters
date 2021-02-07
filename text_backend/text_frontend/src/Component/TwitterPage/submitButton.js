import React, { Component } from "react";
//import Button from '@material-ui/core/Button';
import Button from 'react-bootstrap/Button'

import submitButtonStyle from './Styling/submitButton.module.css'

export default class SubmitButton extends Component {

  render() {
    return (
        <Button variant="outline-primary"
                onClick={this.props.onClick}
                className={submitButtonStyle.default}>
            submit
        </Button>
    );
  }
}