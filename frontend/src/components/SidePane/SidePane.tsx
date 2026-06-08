import './SidePane.css'
import userIcon from '../../assets/user.svg'
import logo from '../../assets/logo.png'

function SidePane() {
    return (
    <>
        <div className="side-pane">
            <div className="sd-header">
                <div className="sd-header-icon">
                    <img src={logo} alt="GB" />
                </div>
                <div className="sd-header-title">
                            German AI Buddy
                </div>
            </div>

            <div className="sd-nav">
                <ul>
                    <li>New Conversation</li>
                    <li>Chat</li>
                    <li>History</li>
                    <li>Mistakes</li>
                    <li>Progress</li>
                    <li>Settings</li>
                </ul>
            </div> 
                
            <div className="sd-user">
                <div className="sd-user-image">
                    <img src={userIcon} alt="user picture" />
                </div>
                <div className="sd-user-name">
                    User
                </div>
                <div className="sd-user-level">
                    A2
                </div>
                <div className="sd-user-bar"></div>
            </div>
        </div>
    </>
    )
}

export default SidePane