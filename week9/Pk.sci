function M=Pk(n,k,v)
    u = householder(v);
    M = eye() - 2*u*u';
    
endfunction

function M = P(n,k,a)
    M = eye(n,n);
    M(k:n,k:n)=Pk(n,k,A(k:n,k))
    
endfunction

function A= p2z(R,theta)
    A = R*exp(%i*%pi*theta/180.0);
endfunction


A = eye(8,8)
for i=1:8
    for j=1:8
        A(i,j)=cos((i-1)*(j-1)*%pi/8.0)
    end
    
end


B = [15 -3 -5 -7;-3 25 -4 -6;-5 -4 10 -5;-7 -6 -5 20];
P = Pk(4,1,B(1:4,1))
B = P*B

//C = [1 1 1 1;1 1 -%i p2z(1,-45);1 p2z(1,45) %i 1]

//for i=1:3
//    Pa = P(4,i,B)
//    B = Pa*B*Pa'
    
//end
//print B