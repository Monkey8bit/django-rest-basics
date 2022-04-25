import React, {useState, useEffect} from "react";
import {Link} from "react-router-dom";
import {useParams} from "react-router-dom";
import axios from "axios";


const SingleUser = () => {
    const userId = useParams().id;
    const [user, setUser] = useState({})
    useEffect(() => {
        const User = () => {
             axios
                 .get(`http://127.0.0.1:8000/api/users/${userId}`)
                 .then(response => setUser(response.data))
                 .catch(error => console.log(error));
        }
        User();
    }, [userId])

    return (
        <ul>
            <h1>{user.username}</h1>
            <li>First name: {user.first_name}</li>
            <li>Last name: {user.last_name}</li>
            <li>Email: {user.email}</li>
        </ul>
    )
}


const UserItem = ({user}) => {
    return (
        <tr>
            <td key={user.id}>{user.id}</td>
            <td><Link to={`/users/${user.id}`}>{user.username}</Link></td>
            <td>{user.first_name}</td>
            <td>{user.last_name}</td>
            <td>{user.email}</td>
            <td>{user.is_superuser.toString().toUpperCase()}</td>
            <td>{user.test_user.toString().toUpperCase()}</td>
        </tr>
    )
}

const UserList = ({users}) => {
    return (
        <table className={"maintable userlist"}>
            <th>Id</th>
            <th>User name</th>
            <th>First name</th>
            <th>Last name</th>
            <th>Email</th>
            <th>Is superuser</th>
            <th>Is test user</th>
            {users.map((user) => <UserItem user={user} />)}
        </table>
    )
}

export default UserList
export {SingleUser}
