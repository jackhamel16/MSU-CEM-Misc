function interaction = main
  rho = 1;
  dr = [1; 1; 1];
  dipole = [1; 2; 3];
  efield = calc_efield(calc_polar(rho),dr);
  interaction = calc_interaction(efield, dipole)
end


function polarization = calc_polar(rho)
  polarization = [rho*2 0 0];
end

function results = calc_efield(polarization, dr)
  mu0 = 1;
  c = 2;
  hbar = 1;
  dist = norm(dr);
  rr = dr * transpose(dr) ./ dist^2;
  irr = eye(3) - rr;
  i3rr = eye(3) - 3*rr;
  
  spatial_dyads = [i3rr.*c^2/dist^3 i3rr.*c/dist^2 irr./dist];
  
  results = zeros(3);
  for i=1:3
      results = results + mu0/(4*pi*hbar) * ...
                   polarization(i) .* spatial_dyads(:,3*i-2:3*i);
  end
end

function interaction = calc_interaction(efield, dip)
  interaction = dot(dip, efield * dip);
end