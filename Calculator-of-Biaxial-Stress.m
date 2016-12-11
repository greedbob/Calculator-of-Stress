% BOBO MATLAB code for bobo.fig
%      BOBO, by itself, creates a new BOBO or raises the existing
%      singleton*.
%
%      H = BOBO returns the handle to a new BOBO or the handle to
%      the existing singleton*.
%
%      BOBO('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in BOBO.M with the given input arguments.
%
%      BOBO('Property','Value',...) creates a new BOBO or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before bobo_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to bobo_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help bobo

% Last Modified by GUIDE v2.5 02-Jun-2016 14:17:53

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @bobo_OpeningFcn, ...
                   'gui_OutputFcn',  @bobo_OutputFcn, ...
                   'gui_LayoutFcn',  [] , ...
                   'gui_Callback',   []);
if nargin && ischar(varargin{1})
    gui_State.gui_Callback = str2func(varargin{1});
end

if nargout
    [varargout{1:nargout}] = gui_mainfcn(gui_State, varargin{:});
else
    gui_mainfcn(gui_State, varargin{:});
end
% End initialization code - DO NOT EDIT


% --- Executes just before bobo is made visible.
function bobo_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to bobo (see VARARGIN)

% Choose default command line output for bobo
handles.output = hObject;

% Update handles structure
guidata(hObject, handles);

% UIWAIT makes bobo wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = bobo_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;



function angle_Callback(hObject, eventdata, handles)
% hObject    handle to angle (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of angle as text
%        str2double(get(hObject,'String')) returns contents of angle as a double


% --- Executes during object creation, after setting all properties.
function angle_CreateFcn(hObject, eventdata, handles)
% hObject    handle to angle (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function b1_Callback(hObject, eventdata, handles)
% hObject    handle to b1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of b1 as text
%        str2double(get(hObject,'String')) returns contents of b1 as a double


% --- Executes during object creation, after setting all properties.
function b1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to b1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function b2_Callback(hObject, eventdata, handles)
% hObject    handle to b2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of b2 as text
%        str2double(get(hObject,'String')) returns contents of b2 as a double


% --- Executes during object creation, after setting all properties.
function b2_CreateFcn(hObject, eventdata, handles)
% hObject    handle to b2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function b4_Callback(hObject, eventdata, handles)
% hObject    handle to b4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of b4 as text
%        str2double(get(hObject,'String')) returns contents of b4 as a double


% --- Executes during object creation, after setting all properties.
function b4_CreateFcn(hObject, eventdata, handles)
% hObject    handle to b4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function b3_Callback(hObject, eventdata, handles)
% hObject    handle to b3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of b3 as text
%        str2double(get(hObject,'String')) returns contents of b3 as a double


% --- Executes during object creation, after setting all properties.
function b3_CreateFcn(hObject, eventdata, handles)
% hObject    handle to b3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on button press in pushbutton1.
function pushbutton1_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
angle = str2num(get(handles.angle,'String'));
angle = angle/180*pi;
b1 = str2double(get(handles.b1, 'String'));
b2 = str2double(get(handles.b2, 'String'));
b3 = str2double(get(handles.b3, 'String'));
b4 = str2double(get(handles.b4, 'String'));
b = [b1,b2;b3,b4];


left=[cos(angle),sin(angle);-sin(angle),cos(angle)];
x=left*b*(left');
zheng=x(1);
qie=x(2);
set(handles.ans1,'String',zheng);
set(handles.ans2,'String',qie);

if (b1==b4)
    zhufangxiang = 0.5*pi;
else
    zhufangxiang=atan(2*b2/(b1-b4))/2;
end

leftzyl=[cos(zhufangxiang),sin(zhufangxiang);-sin(zhufangxiang),cos(zhufangxiang)];
zhuyinglizhuangtai = leftzyl*b*(leftzyl');

zhuyingli1=zhuyinglizhuangtai(1);
zhuyingli2=zhuyinglizhuangtai(4);
set(handles.ans3,'String',zhufangxiang/pi*180);
set(handles.ans41,'String',zhuyingli1);
set(handles.ans42,'String',zhuyingli2);

hold on;
r = sqrt((b1-b4)^2/4+b2^2);
xin = (b1+b4)/2;
plot(xin+r,0,'r*');
plot(xin-r,0,'r*');

hold on;
axis equal;
alpha=0:pi/50:2*pi;
x1 = (b1+b4)/2+ sqrt((b1-b4)*(b1-b4)/4+b2*b2)*cos(alpha);
y1 = sqrt((b1-b4)*(b1-b4)/4+b2*b2)*sin(alpha);
plot(handles.axes1,x1,y1,'g');

hold on;
axis equal;
xin = (b1+b4)/2;
if(xin==b1)
    n=abs(r)/0.01+1;
    x2=ones(1,n);
    x2=xin*x2;
    if(b1>0)
        y2=0:0.01:r;
    else
        y2=r:0.01:0;
    end
else
    if(xin>b1)
    x2 = (b1):0.001:(xin);
    k = 2*b2/(b4-b1);
    else
    x2 = (xin):0.001:(b1);
    k = 2*b2/(b1-b4);
    end
    y2 = k*(x2-xin);
end
plot(handles.axes1,x2,y2,'r');

plot(b1,b2,'r*');
text(b1,b2,[ '  X (' num2str(b1) ',' num2str(b2) ')']);

hold on;
axis equal;
if(xin==zheng)
    n=abs(r)/0.01+1;
    x3=ones(1,n);
    x3=xin*x3;
    if(zheng>0)
        y3=0:0.01:r;
    else
        y3=r:0.01:0;
    end
else
    if(xin>zheng)
    x3 = (zheng):0.001:(xin);
    k = qie/(xin-zheng);
    else
    x3 = (xin):0.001:(zheng);
    k = qie/(zheng-qie);
    end
    y3 = k*(x3-xin);
end
plot(handles.axes1,x3,y3,'b');

plot(zheng,qie,'r*');

%disp(xin);
%disp(r);
quiver(xin-5*r/4,0,3*r,0,'black');
quiver(0,-5*r/4,0,3*r,'black');



% --- Executes during object creation, after setting all properties.
function axes1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to axes1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: place code in OpeningFcn to populate axes1


% --- Executes on mouse press over figure background, over a disabled or
% --- inactive control, or over an axes background.
function figure1_WindowButtonDownFcn(hObject, eventdata, handles)
% hObject    handle to figure1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


% --- Executes on button press in pushbutton2.
function pushbutton2_Callback(hObject, eventdata, handles)
set(handles.ans1,'String','');
set(handles.ans2,'String','');
set(handles.ans3,'String','');
set(handles.ans41,'String','');
set(handles.ans42,'String','');


hold off;
x3=0;
y3=0;
plot(handles.axes1,x3,y3,'w');

clear;

% hObject    handle to pushbutton2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
