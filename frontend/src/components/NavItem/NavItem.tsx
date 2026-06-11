import './NavItem.css';

type NavItemProps = {
  label: string;
  newConversation: boolean;
  icon: string;
  isSelected: boolean;
  onClick: () => void;
};

function determineClassName (newConversation: boolean, isSelected: boolean): string{
    const classes: string[] = ['nav-item'];

    if (newConversation) classes.push('nav-new-conversation');
    if (!newConversation && isSelected) classes.push('nav-selected'); 

    return classes.join(' ');
}

function NavItem({ label, newConversation, icon, isSelected, onClick }: NavItemProps) {
  return (
    <>
        <li className={determineClassName(newConversation, isSelected)} onClick={onClick}>
            <span className="material-symbols-outlined">
                {icon}
            </span>
            <div className='nav-item-label'>{label}</div>
        </li>
    </>
  );
}

export default NavItem;