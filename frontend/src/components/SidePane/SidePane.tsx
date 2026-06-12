import './SidePane.css';
import NavItem from '../NavItem/NavItem';
import userIcon from '../../assets/user.svg';
import logo from '../../assets/logo.png';
import { useState, useEffect } from 'react';


function SidePane() {
    const [selectedItem, setSelectedItem] = useState('Chat');
    const [selectedTheme, setSelectedTheme] = useState('light_mode');

    function toggleTheme() {
        setSelectedTheme(prev =>
            prev === 'dark_mode' ? 'light_mode' : 'dark_mode'
        );
    }

    useEffect(() => {
        document.documentElement.setAttribute(
            'data-theme',
            selectedTheme
        );
    }, [selectedTheme]);

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
                <div className="sd-header-subtitle">
                    Your learning companion
                </div>
            </div>

            <div className="sd-nav">
                <ul>
                    <NavItem 
                        label='New Conversation' 
                        newConversation={true} 
                        icon='add'
                        isSelected={selectedItem === 'New Conversation'}
                        onClick={() => setSelectedItem('Chat')}
                    />
                    <NavItem 
                        label='Chat' 
                        newConversation={false} 
                        icon='forum'
                        isSelected={selectedItem === 'Chat'}
                        onClick={() => setSelectedItem('Chat')}
                    />
                    <NavItem 
                        label='History' 
                        newConversation={false} 
                        icon='history_2'
                        isSelected={selectedItem === 'History'}
                        onClick={() => setSelectedItem('History')}
                    />
                    <NavItem 
                        label='Vocabulary' 
                        newConversation={false} 
                        icon='book_5'
                        isSelected={selectedItem === 'Vocabulary'}
                        onClick={() => setSelectedItem('Vocabulary')}
                    />
                    <NavItem 
                        label='Mistakes' 
                        newConversation={false} 
                        icon='mystery'
                        isSelected={selectedItem === 'Mistakes'}
                        onClick={() => setSelectedItem('Mistakes')}
                    />
                    <NavItem 
                        label='Progress' 
                        newConversation={false} 
                        icon='finance_mode'
                        isSelected={selectedItem === 'Progress'}
                        onClick={() => setSelectedItem('Progress')}
                    />
                    <NavItem 
                        label='Settings' 
                        newConversation={false} 
                        icon='settings'
                        isSelected={selectedItem === 'Settings'}
                        onClick={() => setSelectedItem('Settings')}
                    />
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
                <div className="sd-user-theme">
                    <button className="material-symbols-outlined" onClick={toggleTheme}>
                        {selectedTheme}
                    </button>
                </div>
            </div>

        </div>
    </>
    )
}

export default SidePane