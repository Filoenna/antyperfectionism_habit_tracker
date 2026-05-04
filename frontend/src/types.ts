export interface MenuItem {
  label: string;
  icon?: string;
  command?: (event?: any) => void;
  badge?: string;
  shortcut?: string;
  items?: MenuItem[];
}