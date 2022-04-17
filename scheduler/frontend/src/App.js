import React from "react";
import "./App.css";
import axios from "axios";
import UserList from "./components/User";


class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            "users": []
        }
    }

    componentDidMount() {
        axios
            .get("http://127.0.0.1:8000/api/users/")
            .then(response => {
                let users = response.data;
                this.setState({
                    "users": users
                })
            })
            .catch(error => console.log(error))
    };

    render() {
        return (
            <div className={"container"}>
                <div className={"menu"}>
                    <ul className={"navbar"}>
                        <li><a href={"#"}>Lorem ipsum.</a></li>
                        <li><a href={"#"}>Lorem.</a></li>
                        <li><a href={"#"}>Lorem ipsum dolor.</a></li>
                    </ul>
                </div>
                <div className={"users"}>
                    <UserList users={this.state.users} />
                </div>
                <div className={"footer"}>
                    <p>2022 &copy; GB Scheduler </p>
                </div>
            </div>
        )
    };
}


export default App;
