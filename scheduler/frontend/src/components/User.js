import React from "react";


const UserItem = ({user}) => {
    return (
        <tr>
            <td key={user.id}>{user.id}</td>
            <td>{user.username}</td>
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
        <table className={"userlist"}>
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
