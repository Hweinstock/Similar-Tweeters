import React, { Component } from "react";
import Form from 'react-bootstrap/Form'

export default class InputBox extends Component {
    render() {
        return (
            <div>
                <Form>
                    <Form.Group>
                        <Form.Control type="twitter_handle"
                                      placeholder="Enter username"
                                      size="lg"
                                      className="w-25"/>
                    </Form.Group>
                </Form>
            </div>
        );
    }
}
